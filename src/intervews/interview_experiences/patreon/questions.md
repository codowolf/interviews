# Design Shopping Cart Coupon
Excellent question. This gets to the very core of object-oriented design, specifically the principle of **Separation of Concerns**.

Your proposal is intuitive: if a coupon applies to an item, why not put it on the item? Let's analyze this design and then compare it to the one I proposed.

### Analysis of Your Proposed Design

```python
# Your proposed structure
class Coupon:
  id: int
  type: str
  def compute_price(item_price, total_quantity): ...

class Item:
  id: str
  name: str
  original_price: float
  applicable_coupons: list[Coupon] = [] # List of available coupons
  
  def get_best_coupon(): ...
  def get_final_price_after_coupon(quantity): ... # Needs quantity
```

**Pros of this approach:**

*   **Encapsulation:** It seems to encapsulate all logic related to an item's price within the `Item` class itself.

**Cons and Design Challenges:**
1.  **Violation of Single Responsibility Principle:** The `Item` class now has two very different jobs.
    *   Job 1: Represent a product in the catalog (its name, its base price). This is pure data.
    *   Job 2: Act as a calculator for complex, context-dependent promotional pricing. This is business logic.
    A class should have only one reason to change. With this design, you'd change the `Item` class if the product details change (e.g., price update) AND if the rules for calculating discounts change.
2.  **The Context Problem:** This is the most significant issue. An `Item` object on its own lacks the necessary **context** for many real-world coupons.
    *   Your `compute_price` method takes `item_price` and `total_quantity`. This works for simple coupons.
    *   But what about our "Buy a loaf of bread, get 50% off butter" coupon? When you call `butter.get_final_price_after_coupon()`, the `butter` object has no way of knowing if bread is in the cart. You would be forced to pass the entire `ShoppingCart` object into the `Item`'s method, like this: `butter.get_final_price(quantity, cart)`. This creates a messy circular dependency where the cart holds items, and items need to know about the cart.
3.  **State Management:** An `Item` in a catalog is different from an "item in a cart".
    *   The `Item` in the catalog represents the platonic ideal of "apple" with its base price of $1.00.
    *   The entry in the shopping cart represents "10 apples that I, the shopper, am currently buying."
    Your design merges these two concepts. The `ShoppingCart` should be responsible for managing the state of the *transaction* (quantities, applied coupons), while the `Item` should just represent the product.

### Item-Level vs. Cart-Level Coupons

You asked the perfect follow-up question: **"Is a coupon applied at the item level or cart level?"**

The answer is **both**, and a robust design must gracefully handle this distinction. This is where the weakness of putting coupons on the `Item` becomes most apparent.

*   **Item-Level Coupon:** "10% off apples." This coupon's logic only needs to know about the item it's applied to.
*   **Cart-Level Coupon:** "$10 off your entire purchase of $50 or more." This coupon cannot be attached to any single `Item`. Its logic depends on the subtotal of the *entire cart*.

The original design I proposed (where the `ShoppingCart` orchestrates the pricing) can be easily extended to handle both types. The design where the `Item` calculates its own price cannot handle cart-level coupons at all without significant and awkward modifications.

### Recommended (Refined) Architecture

Let's stick with the **Separation of Concerns** model.

1.  **`Item` (The Data):** Remains a simple, stateless data class. It represents a product in the catalog. It knows its name and its base price. It knows nothing about coupons or shopping carts.
    ```python
    @dataclass(frozen=True)
    class Item:
        name: str
        price: float
    ```

2.  **`Coupon` (The Logic/Strategy):** An interface that defines a `calculate_discount` method. This makes the system pluggable for new coupon types. To handle more complex scenarios, we give it all the context it could possibly need.
    ```python
    class Coupon(ABC):
        @abstractmethod
        def calculate_discount(self, cart: 'ShoppingCart', item_name: str) -> float:
            # Note: We pass the whole cart for context, and the item_name
            # this coupon is being evaluated for.
            pass
    ```

3.  **`ShoppingCart` (The Context/Orchestrator):** It holds the state of the current transaction. It knows which items are in the cart, their quantities, and which coupons have been applied. **Its primary job is to orchestrate the final price calculation.**

Here's how the `ShoppingCart` would handle both coupon types:

```python
class ShoppingCart:
    def __init__(self, item_catalog: dict[str, Item]):
        self._item_catalog = item_catalog
        self._items: dict[str, int] = {} # Item name -> quantity
        
        # We now have TWO types of coupon lists
        self._item_coupons: dict[str, list[Coupon]] = {} # For item-level coupons
        self._cart_coupons: list[Coupon] = []           # For cart-level coupons
    
    # ... add_item, remove_item methods ...
    
    def apply_item_coupon(self, item_name: str, coupon: Coupon):
        # Applies a coupon to a specific item line
        if item_name not in self._item_coupons:
            self._item_coupons[item_name] = []
        self._item_coupons[item_name].append(coupon)

    def apply_cart_coupon(self, coupon: Coupon):
        # Applies a coupon to the whole cart
        self._cart_coupons.append(coupon)

    def calculate_total(self) -> float:
        # Step 1: Calculate the subtotal after item-level discounts
        subtotal = 0.0
        for item_name, quantity in self._items.items():
            item = self._item_catalog[item_name]
            base_price = item.price * quantity
            
            # Find the best item-level discount for this line item
            best_item_discount = 0.0
            if item_name in self._item_coupons:
                discounts = [c.calculate_discount(self, item_name) for c in self._item_coupons[item_name]]
                best_item_discount = max(discounts) if discounts else 0.0
            
            line_item_price = max(0, base_price - best_item_discount)
            subtotal += line_item_price
        
        # Step 2: Calculate and apply the best cart-level discount
        best_cart_discount = 0.0
        if self._cart_coupons:
            # Note: A cart-level coupon's calculate_discount would need to know the subtotal.
            # This requires a slight change to the interface or how it's called.
            # For simplicity here, let's assume it can figure it out from the cart object.
            cart_discounts = [c.calculate_discount(self, item_name=None) for c in self._cart_coupons]
            best_cart_discount = max(cart_discounts) if cart_discounts else 0.0

        # Step 3: Return the final price
        grand_total = max(0, subtotal - best_cart_discount)
        return grand_total
```

### Conclusion

While putting `applicable_coupons` on the `Item` is a tempting simplification, it tightly couples unrelated concerns and breaks down as soon as you introduce coupons that require broader context (like multi-item or cart-total coupons).

By keeping `Item`, `Coupon`, and `ShoppingCart` as separate, distinct concepts, you create a far more robust, scalable, and maintainable system that mirrors the reality of how retail promotions work. **The `ShoppingCart` is the orchestrator that uses `Coupon` strategies to calculate the final price of the `Item` data it contains.**
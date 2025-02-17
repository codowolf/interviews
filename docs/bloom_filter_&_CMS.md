### **Bloom Filter Summary**

#### **What is a Bloom Filter?**

- A **probabilistic data structure** to test if an element is in a set.
- **Space-efficient** but allows **false positives** (says an item is in the set when it’s not). No false negatives.
- Used in caching, spell checkers, network routers, and databases to quickly filter out non-members.

---
#### **How It Works**

1. **Bit Array**: A fixed-size array of bits (e.g., `[0, 0, 0, 0, 0]`).
2. **Hash Functions**: Multiple hash functions map an item to positions in the bit array.
3. **Add Item**: Hash the item with each hash function, use **modulo** to map the hash to a bit array index, and set the corresponding bit to `1`.
4. **Check Item**: Hash the item, use **modulo** to map the hash to a bit array index, and check if all corresponding bits are `1`. If any bit is `0`, the item is **definitely not** in the set. If all bits are `1`, the item is **probably** in the set.
---
#### **Example**

- **Bit Array Size**: 10 bits (`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`).
- **Hash Functions**: 3 hash functions.
- **Add "apple"**:
    - Hash "apple" with each hash function:
        - Hash 1: `hash("apple0") % 10` → `2`
        - Hash 2: `hash("apple1") % 10` → `5`
        - Hash 3: `hash("apple2") % 10` → `9`
    - Set bits at positions `2, 5, 9` to `1`:
        - Bit array: `[0, 0, 1, 0, 0, 1, 0, 0, 0, 1]`.
- **Check "apple"**:
    - Hash "apple" with each hash function:
        - Hash 1: `hash("apple0") % 10` → `2`
        - Hash 2: `hash("apple1") % 10` → `5`
        - Hash 3: `hash("apple2") % 10` → `9`
    - Check bits at positions `2, 5, 9`:
        - All bits are `1` → **Probably in set**.
- **Check "orange"**:
    - Hash "orange" with each hash function:
        - Hash 1: `hash("orange0") % 10` → `2`
        - Hash 2: `hash("orange1") % 10` → `4`
        - Hash 3: `hash("orange2") % 10` → `7`
    - Check bits at positions `2, 4, 7`:
        - Bit `4` is `0` → **Definitely not in set**.

---

#### **Hashing and Setting Bits**

- **Hashing**: Convert an item (e.g., "apple") to an integer using a hash function (e.g., MD5).
- **Modulo Operation**: Use `%` to map the hash to a bit array index.
```python
# hash of "apple" + "0" = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
hashofword = hashlib.md5(item.encode('utf-8') + str(seed).encode('utf-8'))

# 2134213421342134213421342134213421342134
large_number = int(hashofword.hexdigest(), 16) 

# 3
index = large_number % size
```
- `hashlib.md5`: Creates an MD5 hash of the item combined with a seed.
- `int(..., 16)`: Converts the hexadecimal hash to an integer.
- `% size`: Maps the integer to a bit array index using modulo.
---

### Real-World Sizes

Here are some examples of Bloom filter sizes for different scenarios:

|**Number of Items (n)**|**False Positive Rate (p)**|**Bit Array Size (m)**|**Memory Usage**|
|---|---|---|---|
|1,000,000|1% (0.01)|~9.6 million bits|~1.2 MB|
|10,000,000|1% (0.01)|~96 million bits|~12 MB|
|100,000|0.1% (0.001)|~1.4 million bits|~175 KB|
|1,000,000|0.1% (0.001)|~14.4 million bits|~1.8 MB|
#### **Key Points**

- **Space-efficient**: Uses a bit array, not the actual data.
- **False positives**: Possible, but tunable by adjusting bit array size and hash functions.
- **No false negatives**: If the Bloom filter says an item is not in the set, it’s definitely not.

---

### **Interview Prep**

- **Use Case**: "I used a Bloom filter to reduce database lookups by quickly filtering out non-existent keys."
- **Trade-offs**: "It’s space-efficient but allows false positives, which is acceptable in my use case."
- **Example**: "For 1M items with a 1% false positive rate, the bit array size is ~9.6M bits (~1.2MB)."

Not quite! While **Count-Min Sketch** and **Bloom Filter** are both probabilistic data structures and share some similarities, they serve **different purposes** and have **key differences**. Let’s break it down:

---

### **Bloom Filter**
- **Purpose**: Tests whether an element is in a set.
- **Data Structure**: A bit array of size `m` and `k` hash functions.
- **Operations**:
  - **Add**: Hash the item with `k` hash functions, set the corresponding bits to `1`.
  - **Check**: Hash the item, check if all corresponding bits are `1`. If any bit is `0`, the item is **definitely not** in the set. If all bits are `1`, the item is **probably** in the set.
- **False Positives**: Possible (says an item is in the set when it’s not).
- **False Negatives**: Not possible (says an item is not in the set when it is).
- **Use Cases**: Membership testing, spell checkers, network routers, caching.

---

## **Count-Min Sketch**
- **Purpose**: Estimates the frequency (count) of elements in a stream.
- **Data Structure**: A 2D array of counters (size `d x w`) and `d` hash functions.
- **Operations**:
  - **Add**: Hash the item with `d` hash functions, increment the corresponding counters in each row.
  - **Query**: Hash the item, retrieve the minimum value among the corresponding counters. This is the estimated frequency of the item.
- **False Positives**: Overestimates the count (due to hash collisions).
- **False Negatives**: Not possible (counts are never underestimated).
- **Use Cases**: Frequency estimation, heavy hitters problem, stream processing.

---

### **Key Differences**
| Feature             | Bloom Filter                     | Count-Min Sketch                        |
| ------------------- | -------------------------------- | --------------------------------------- |
| **Purpose**         | Membership testing               | Frequency estimation                    |
| **Data Structure**  | Bit array (1 array for all hash) | 2D array of counters (1 array per hash) |
| **Operations**      | Set bits, check bits             | Increment counters, query counts        |
| **False Positives** | Possible (membership)            | Possible (overestimated counts)         |
| **False Negatives** | Not possible                     | Not possible                            |
| **Use Cases**       | Caching, spell checkers          | Stream processing, heavy hitters        |

---

### **Why Count-Min Sketch is Not Just a Bloom Filter with Counts**
1. **Different Data Structures**:
   - Bloom Filter uses a **bit array** to represent membership.
   - Count-Min Sketch uses a **2D array of counters** to represent frequencies.

2. **Different Operations**:
   - Bloom Filter sets and checks bits.
   - Count-Min Sketch increments and queries counters.

3. **Different Use Cases**:
   - Bloom Filter answers **"Is this item in the set?"**.
   - Count-Min Sketch answers **"How many times has this item appeared?"**.

4. **False Positives**:
   - Bloom Filter’s false positives are about membership.
   - Count-Min Sketch’s false positives are about overestimating counts.

---

### **Example: Bloom Filter vs. Count-Min Sketch**

#### Bloom Filter Example
- **Bit Array Size**: 10 bits (`[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`).
- **Hash Functions**: 3 hash functions.
- **Add "apple"**:
  - Hash "apple" → positions `2, 5, 9`.
  - Set bits: `[0, 0, 1, 0, 0, 1, 0, 0, 0, 1]`.
- **Check "apple"**:
  - Hash "apple" → positions `2, 5, 9`.
  - Check bits: All are `1` → **Probably in set**.

#### Count-Min Sketch Example
- **2D Array Size**: 3 rows x 10 columns (all counters initialized to `0`).
- **Hash Functions**: 3 hash functions.
- **Add "apple"**:
  - Hash "apple" → positions `2, 5, 9` in each row.
  - Increment counters:
    - Row 1: `[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]`
    - Row 2: `[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]`
    - Row 3: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]`
- **Query "apple"**:
  - Hash "apple" → positions `2, 5, 9` in each row.
  - Retrieve counts: `1, 1, 1`.
  - Estimated count: `min(1, 1, 1) = 1`.

---

### **When to Use Which?**
- Use a **Bloom Filter** when:
  - You only need to check if an item is in a set.
  - Space efficiency is critical.
  - False positives are acceptable.

- Use a **Count-Min Sketch** when:
  - You need to estimate the frequency of items in a stream.
  - Overestimating counts is acceptable.
  - You’re dealing with large-scale data streams.

---

### **Summary**
- **Bloom Filter**: Membership testing with a bit array.
- **Count-Min Sketch**: Frequency estimation with a 2D counter array.
- They are **not the same**, but both are probabilistic and useful for different problems.


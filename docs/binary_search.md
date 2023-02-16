# Tips
- Follow this link on stackoverflow - https://stackoverflow.com/a/54374256 

# Code
## Binary Search (Java)
```java
public static int binarySearch(int[] arr, int target) {
    // Returns first value greater than or equal to target. 
    int start = 0;
    int end = arr.length - 1;
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (arr[mid] < target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    // When loop exits, end < start, so
    // Everything left of start is less than target
    // Everything right of end (including start) is greater than or equal to target
    return start; // or end + 1
}
```
- Returns first value greater than or equal to target. 
- If all elements are equal, return 1st instance
- If target not found, returns `0` or `arr.length`
- Examples
  1. `target = 5`, `arr = [3, 3, 5]` --> `2`
  2. `target = 3`, `arr = [3, 3, 3]` --> `0`
  3. `target = 6`, `arr = [3, 3, 5]` --> `3` (arr.length)
  4. `target = 2`, `arr = [3, 3, 5]` --> `0`
- **NOTE** : For general usage, the output of this program should still be checked for validity. As you can see above, 3 is `index out of bound` and 4 is first item greater than target item.

## Variations
1. `if (arr[mid] < target) start = mid + 1;`
   - return `start; // or end + 1;`
     - returns first items equal or greater than target
   - return `start - 1; // or end;`
     - returns first item less than target
3. `if (arr[mid] <= target) start = mid + 1`
   - return `start; // or end + 1;`
     - returns first item ~~equal or~~ greater than target
   - and so on ... 

# Min Max Problem
These are the problems where you have to minimize the maximum value
> minimized largest sum of the split

> minimum capacity to hold maxium

Usually an array is given with an integer `k`

**NOTE**: this problem only makes sense if ordering of the elements has to be maintained. Otherwise, sorting the array makes sense. 

```java
public int splitArray(int[] nums, int k)

public int shipWithinDays(int[] weights, int days)

public int smallestDivisor(int[] nums, int threshold)

public int maximumCandies(int[] candies, long k)

public int minCapability(int[] A, int k)
```

# Examples
- [2226. Maximum Candies Allocated to K Children](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/discuss/1908888/JavaC%2B%2BPython-Binary-Search-with-Explanation)
- [1802. Maximum Value at a Given Index in a Bounded Array](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1119801/Python-Binary-Search)
- [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/discuss/779999/JavaC++Python-O(logN))
- [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/686316/javacpython-binary-search)
- [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/446376/javacpython-bianry-search)
- [1231. Divide Chocolate](https://leetcode.com/problems/divide-chocolate/discuss/408503/Python-Binary-Search)
- [1011. Capacity To Ship Packages In N Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/javacpython-binary-search/)
- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/discuss/152324/C++JavaPython-Binary-Search)
- [774. Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/discuss/113633/Easy-and-Concise-Solution-using-Binary-Search-C++JavaPython)
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
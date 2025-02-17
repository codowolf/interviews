# Tips
- Follow this link on stackoverflow - https://stackoverflow.com/a/54374256 

# Code
## Binary Search (Python)
```python
def binary_search(arr, int target):
  low, high = 0, len(arr) - 1

  while low <= high:  # to handle case where arr=[1]
    mid = low + (high - low) // 2  # note that mid is always "strictly" decreasing until it's 1

    if target <= arr[mid]:  # this is the answer block because of "="
      high = mid - 1        # when answer if found, we still go left
    else:                   # (so final answer is high + 1 or low)
      low = mid + 1
  
  return low  # or high + 1
```
- Binary search goal is to move towards the answer's half
- The important to think about is where does low and high stay, when loop exits
- `<= or >=` is the block where answer was found but still continued
- This is done for "insert" position, but can also be used to find target
- ex: `tgt=5; arr=[1,3,4,5,9]` (for target being present in the arr)
  - `mid=4; low=1, high=9` action=`low=mid+1` ie `low=5`
  - `mid=5; low=5, high=9` action=`high=mid-1` ie `high=5`
  - `mid=5; low=5, high=5` action=`high=mid-1` ie `high=4`
    - `low=5, high=4` loop terminates cuz `high>low`
    - so answer is at low, or high + 1
- ex: `tgt=2; arr=[1,3,4,5,9]` (for target ABSENT in the arr)
  - `mid=4; low=1, high=9` action=`high=mid-1` ie `high=3`
  - `mid=1; low=1, high=3` action=`low=mid+1` ie `low=3`
  - `mid=3; low=3, high=3` action=`high=mid-1` ie `high=1`
    - `low=3, high=1` loop terminates cuz `high>low`
    - so answer is at low, or high + 1 (which is insertion poistion for 2)
- Let's see behavior with duplicates
  - The above logic always finds the position of the first target
    - Because of `arr[mid] <= target: high = mid - 1`
    - ie, we keep moving left
  - To find the right most target value
    - Code should change to `arr[mid] < target: high = mid - 1` 
    - This ensures that when equal, we move to right `low = mid + 1`
- For insertion problems, the answer is
  - everything left is `"strictly less"`
  - everything right is `"strickly increasing"`
    - with duplicates, it's `"non decreasing"`
> [!tip] **NOTE**: the final index can still be out of bound, so always check bounds
 > - ex: `tgt=5, arr=[1]`, `output_index=1` out of bound
 > - ex: `tgt=0, arr=[1]`, `output_index=-1` out of bound, but in python this is last index. so be extra careful

### Where the above logic (of bounds) will not be applicable 
- https://leetcode.com/problems/search-in-rotated-sorted-array/
- In this problem, if you want to find a pivot as first step, the bounds doesn't work
- It's because essentially the array has two sorted lists
- So bounds has to be adjusted
```python
def get_pivot():
  low, high = 0, len(nums) - 1
  while low < high:  
      mid = low + (high - low) // 2
      if nums[mid] <= nums[high]:
          # can't go out of bound, cuz low < high
          # AND mid is always decreasing until size is 1, but then loop exits
          high = mid  
      else:
          low = mid + 1
  return low
```
- Why this works? 
  - [Because](https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/14425/concise-o-log-n-binary-search-solution) 


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
# Tips
- When the loop ends, the indicators are "low" and "high"
- Follow this link on stackoverflow - https://stackoverflow.com/a/54374256 
- int low = 0, high = Integer.MAX_VALUE;

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
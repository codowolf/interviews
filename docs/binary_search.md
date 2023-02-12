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
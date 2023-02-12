# Tips
- When the loop ends, the indicators are "low" and "high"
- Follow this link on stackoverflow - https://stackoverflow.com/a/54374256 
- int low = 0, high = Integer.MAX_VALUE;

# Code
## Binary Search (Java)
```java
public static int binarySearch(int[] arr, int target) {
    int start = 0;
    int end = arr.length - 1;
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (arr[mid] <= target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    // When loop exits, end < start, so
    // Everything left of start is less than target
    // Everything right of end (including start) is greater than or equal to target
    return start;
}
```
- So in the above algo, the returned value is the first value greater than or equal to target. 
- If target is 5, then in an array `[1,2,5,5,10,11]` it returns index of 1st 5
- Similarly, in array `[1,2,6,10,11]` it returns index of 6
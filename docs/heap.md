```python
heapq.heapify(arr) # ➙ O(log(n))
heapq.heappush(arr, 10) # ➙ O(log(n))
heapq.heappop(arr) # ➙ O(log(n))

# heapify is essentially every element at the top layer is less than the elements below that layer
# But for the same level, it's not sorted
    0
   4 2
  7 8 6
 30 40 60
```
##### Carry over heap

> [!tip] **Don't Forget**:  In some cases, the value of heap item popped will be carried over to the heap item being added

For example, [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) in this problem, the max of the popped item is added to the item being added to the heapq

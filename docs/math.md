# Math related to the problems

## Sets
- Number of subsets including empty set given N = `2^n`
  - Every item you add, the total number doubles
    - This is because, think of it as a binary tree. Every item you add, it branches out into itself and with the new value added. 
    - ex: for a set {1, 2} = {}, {1}, {2}, {1, 2}
      - Here 3 would be added to each item {3}, {1, 3}, {2, 3}, {1,2,3} for form K new items. Total would be `total = total + total`

## Subarrays
- Total subarrays of length N, would be Summation of N = `N * (N + 1) / 2`
  - Because, everytime you add an element, you can form subarry with all elements to the left. 
  - [1,3,5]; Say you add 6 to this
  - Then new ones would be [1,3,5,6], [3,5,6], [5,6], [6] = 4 new subarrays
  - So if array had only one element, then it's 1
    - 2 elements - 2 new subarrays, 3 elements - 3 new subarrays and so on
    - so `1 + 2 + 3 + 4 ... N`
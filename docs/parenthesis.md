# Tips
Apparently parenthesis problems are a thing. Look at 2116 example solutions. 
The general trick on parenthesis "validation" problem is to do left to right check and right to left check doing balancing. 
Balancing is incrementing count when you incurr "(" and decrementing count when you incurr ")". At any point if count becomes negative then it's invalid and terminal state.

The idea is that whenever the count of closing bracket is higher than the opening, there's no way you can balance it by adding opening brackets later becuase it's already invalid. 
For problem 2116, check parenthesis can be valid, you just have to check the balance from both ends.

# Examples
- [2116. Check if a Parentheses String Can Be Valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/)
Slightly different version of `hit counter` but idea is the same

# Question
Loans enter the system at different times. What is the total amount of loans in the last hour?
For example, [100, 2:15pm], [150, 3:05pm], [200, 4:05pm]
If the data is read at 2:30pm, the result is 100.
If the data is read at 3:05pm, the result is 250.
If the data is read at 3:45pm, the result is 150.
If the data is read at 4:05pm, the result is 350. This question


does not seem to be the original question of LC. I have run the test cases and I feel there is no problem.
The follow-up is an open question. If the memory is very small and cannot store all the data, how should I read the amount of loans in the last hour?
I did not write it out because I did not have enough time.


# Solution
- Use a double ended queue 
- minute granularity
- if last time in queue is with same timestamp, then just increment. Add the value to `total_loan` attribute
- upon read, invalidate the queue for invalid time stamps. Keep a `total_loan` and update the sum as needed



https://leetcode.com/problem-list/mzw3cyy6/ 

> [!tip] Main Algo 
> - Usually consists of a 1d line, and ranges
>   - start, end = range
> - for entire plain of range,
>   - `dp[start] += 1`
>   - `dp[end] -= 1`
> - for entire plain of range, prefix-sum it — meaning, add them like a line sweep
>   - `dp[i] += dp[i - 1]`


Here's code for population

```python
def maximumPopulation(self, logs: List[List[int]]) -> int:
  """
  Given population log of (birth, death),
  return earliest year with max population
  - Range 0 to 2051
  """

  pop = [0] * 2051
  for b, d in logs:
    pop[b] += 1 # increase population
    pop[d] -= 1 # decreate population
  
  res = 0
  for i in range(1, len(pop)):
    pop[i] += pop[i - 1] # sweep add them
    if pop[i] > pop[res]: # select max
      res = i
  return res
```


# SLIDING WINDOW PROBLEMS

Template for solving problems where you need to keep a count while iterating pointers. Usually this template is for string based problems

```python
    # find longest substring with no repeated characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_count = defaultdict(int)
        left, right = 0, 0
        window_size = 0
        while right < len(s):
            c = s[right]
            window_count[c] += 1

            while window_count[c] > 1:
                window_count[s[left]] -= 1
                left += 1
            
            window_size = max(window_size, right - left + 1)
            right += 1

        return window_size
```

[List of problems of sliding window](https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/c-maximum-sliding-window-cheatsheet-template/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days)


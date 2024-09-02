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
                left = left + 1
            
            window_size = max(window_size, right - left + 1)
            right = right + 1

        return window_size

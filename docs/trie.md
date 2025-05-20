```python
class TrieNode:
  def __init__(self):
    self.links = [None] * 26
    self.word = None

class Solution:
  def __init__(self):
    self.root = TrieNode()

  def add_word(self, word: str):
    temp = self.root
    i = 0
    while temp:
      idx = ord(word[i]) - ord('a')
      if not temp.links[idx]:
        temp.links[idx] = TrieNode()
      temp = temp.links[idx]
      i += 1
    temp.word = word

```

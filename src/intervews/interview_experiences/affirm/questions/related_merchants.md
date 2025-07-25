
# Questions
Input: A series of users' shopping history, recording the merchants where the users have made purchases.
A list of lists

Objective: For each merchant, find out which other merchants appear most frequently with it in the user's shopping history.

Output: A dictionary where each key is a merchant and the value is a list of other merchants that are most frequently co-purchased with that merchant, sorted by frequency.

# Solution

`user_to_seller_map = {user_id: set(merchants)}`
`seller_to_sellers_map = {merchant_id: set(merchants)`

```python
for user, merchants in user_to_seller_map.items():
	m_list = [e for e in merchants]
	for i in range(len(m_list)):
		for j in range(i + 1, len(m_list)):
			seller_to_sellers_map[m_list[i]][m_list[j]] += 1  # counts frequency
			seller_to_sellers_map[m_list[j]][m_list[i]] += 1
		
```
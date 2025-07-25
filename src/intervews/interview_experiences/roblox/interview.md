# Hiring Manager
- Team — Developer Monetization
	- Interact with ML teams
	- Handles Receipts
	- Handles Pricing?
	- Pricing is sister team
	- Coding Heavy
	- 8 engineers, only one of them close to Principal

# Phone System Design
```
Design a highly scalable, real-time system for a **staff-level system design interview**. Focus on the core architectural components, data flow, and critical trade-offs for supporting immense concurrent user interactions and maintaining low latency under peak global load, typical of a high-volume, interactive platform. Create mermaid chart for HLD as needed.
```

> Interviewer: Harprit Singh

Design a like-unlike system where users can like and unlike an item. 
- As a user, I want to be able to Like and Unlike an item (100k QPS)
- As a user, I want to be able to know if an Item is liked by me (1M QPS)
- As a user, I want to know total likes an item has (1M QPS)
	- When I like the item, I should see my like being reflected


- Interviewer was silent throughout the interview 
- Missed calling out ordering requirement for Like/Dislike in the queue
- HotKey can be handled on writes by adding suffixes 
```json
- Data Model
	- User
	- Item
	- Likes
		- user_id: HASH_KEY
		- item_id: RANGE_KEY
		- like_type: LIKED | UNLIKED
		- liked_at
	- AggregatedLikes
		- item_id
		- likes_count
```

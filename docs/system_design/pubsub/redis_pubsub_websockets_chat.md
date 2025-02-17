#### Main Points
- **push** based ➙ subscriber **pushes** message to redis, redis pushes **message** to subscribers
- if subscriber is down or disconnected, those messages are lost
	- hence at most once delivery
- in a chat system, this subscriber can be a websocket_server
	- partition_key in this case is generally "group_id" ➙ essentially batching messages


###### Examples of subscribers on Redis
- A Websocket server can subscribe to messages based on — group_id:region
	- receive a message from redis
	- load all users it needs to forward to
	- send messages to all users who are connected
		- before sending, it can also check for offline messages per user
	- offline users
		- tell chat server to mark the message as not delivered-> offine 


![User Connection And Reconnection](chat_img3.png "User Connection")
1. User connects to a WSS
2. WSS checks redis user groups to subscribe to
3. Subscribes to all groups, and starts to receive any new message

![User New Group Registry](chat_img4.png "User New Group Registry")
1. while they're connected, a new group is added by chatserver (say they joined a chat room)
2. WSS is notified of it through pub/sub
3. WSS subscribes to the new group for that user (same applies for deletion)

![User Message Publishing](chat_img1.png "User Message Publishing")

![User Disconnected](chat_img2.png "User Disconnected")
1. when WSS can't find a connection to a user for that particular group 
2. it tells CS that particular message should go to inbox for later delivery


#### Scaling the above to multiple regions
1. WSS and Redis are partitioned based on regions
	1. group_id_1:usa ➙ goes to Redis USA cluster
	2. user_id_1:usa ➙ connects to wss_usa instance
	3. wss_usa checks Redis USA for user groups and subscribes to it
2. CS should decide where to route to based on region
3. Rest of it works as usual

Coding: This should be a new question. An event list, processed as required. Part 1 is debugging, with 4 cases. However, there were some problems with the system, and the files of the last two cases were too large to see the content. Later, the interviewer found them himself and pasted them into the question. The bug was easy to find. Pay attention to a few points:
Filter with event_type
Determine whether the key of the map structure in detail exists.

Part 2 is to give you the logic of handling events and let you implement it. The tricky part is that you need to write the logic of parsing screen input by yourself. I asked Google to find it. But the IDE I used for the interview, Jackson, doesn’t support it, so the interviewer posted a gson code for me. I finally wrote it, but it took too long to import the dependency, so I only had time to run the test case given in the question. I don’t know if there will be a part 3 or something later.

**Design: Design the data model of Venmo. There was a misunderstanding at the beginning. One was about how to design data consistency.**
In fact, it is to design the table structure of the database to support 3 scenarios:
1. A transfers money to B using the account balance, and then B withdraws (note that the withdraw here means transferring money from B's venmo to Bank)
2. A transfers money to B using the bank. Then B withdraws before the bank transfer is clear. The bank transfer is finally successful.
3. A transfers money to B through a bank. Then B withdraws before the bank transfer is clear. The bank transfer eventually fails.



| transaction_id | parent_id | sender_id | receiver_id | src_acc | dest_acc | val  | status  |
| -------------- | --------- | --------- | ----------- | ------- | -------- | ---- | ------- |
| 1001           | 1001      | A         | B           | A_BAL   | B_BAL    | +100 | PENDING |
|                |           |           |             |         |          |      |         |
|                |           |           |             |         |          |      |         |

|user_id|balance|
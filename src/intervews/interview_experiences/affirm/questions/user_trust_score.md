# Question
Two questions on the same question
## Part 1
Input two log files representing two days’ logs, the schema is
`<date, user id, order type, amount>`
The user id needs to appear on both days, and there must be at least two unique order types, eg. phone, web, app. Return a list of user ids that meet the requirements

## Part 2
After reading the logs, calculate the trust score of the user in the new purchase
input (user id, order type, amount)
The score calculation consists of two parts:
If you have seen the order type before, you get 50 points. If you have not seen it before, you get 0 points.
If the amount is between the minimum and maximum amounts in the user purchase record, 50 points are awarded. If it is less than the minimum, or greater than the maximum, 10 points are deducted for every 10% difference.

Return the trust score of the sum of the two parts.

## Part 3
Another extension question is asked, what if it is not a log file, but a stream of logs?


# Solution
## Part 1
`{user_id: {order_type: [(date, amount)]}}`

## Part 2
`{user_id: {order_type: [(date, amount)], min_amount: int, max_amount: int}} `

```json
{
  user_id: {
    order_type1: [(date1, amount1), (date2, amount2)],
    order_type2: [(date3, amount3)],
    "min_amount": float,
    "max_amount": float,
    "dates_seen": set(),
    "current_score": int (optional)
  }
}

{
  "u1": {
    "web": [("2023-06-27", 100), ("2023-06-28", 110)],
    "app": [("2023-06-27", 120)],
    "phone": [("2023-06-28", 130)],
    "min_amount": 100,
    "max_amount": 130,
    "dates_seen": {"2023-06-27", "2023-06-28"}
  },
  "u2": {
    "app": [("2023-06-28", 200)],
    "min_amount": 200,
    "max_amount": 200,
    "dates_seen": {"2023-06-28"}
  }
}
```




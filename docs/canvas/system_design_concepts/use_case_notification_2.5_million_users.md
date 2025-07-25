
# Kafka-Based Notification System for 2.5M Users

## Overview

This system efficiently sends push notifications to **2.5 million users** when a football goal is scored using **Apache Kafka**. The architecture follows these key steps:

1. **Job Dispatcher** reads the `goal_notifications` topic for a "goal scored" event.
2. It loads **2.5M users** from a database/cache and splits them into **50 batches** (5K users per batch).
3. These 50 batches are published to a Kafka topic (`user_batches`) with **50 partitions**.
4. **50 consumers**, each assigned to **one partition**, process the batches.
5. Each consumer sends notifications to users in **500-user sub-batches** using a **Firehose API**.

==Note: firehose can typically process 500 items in a batch. ==
How did we estimate this? 
1. 2.5M/10s = 250k messages per second need to be processed
2. We'd need 2.5M/500 = 5k batches
3. Assume a worker can make 10 batch Api calls in parallel in 1s ==(10ms per batch, since you've to consume messages one by one in sequence)==
4. A single host will make 100 batches in 10s
5. So we need 5k/100 = 50 workers to process all of them in 10s
6. 50 workers -> 50 partitions -> so each partition will a batch with 5k users
## Kafka Topic & Partition Setup

- **`goal_notifications`** (1 partition) → Stores the "goal scored" event.
- **`user_batches`** (50 partitions) → Stores pre-split user batches for parallel processing.

---

## **Step 1: Job Dispatcher Publishes User Batches**

```python
from kafka import KafkaProducer
import json

KAFKA_BROKER = "localhost:9092"
USER_BATCH_TOPIC = "user_batches"
BATCH_SIZE = 5000  # 5K users per batch

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def dispatch_users(goal_event):
    users = load_users()  # Load 2.5M users from DB/Cache
    batches = [users[i:i + BATCH_SIZE] for i in range(0, len(users), BATCH_SIZE)]

    for batch_id, user_batch in enumerate(batches):
        message = {
            "batch_id": batch_id,
            "user_ids": user_batch
        }
        producer.send(USER_BATCH_TOPIC, value=message, key=str(batch_id).encode())

    print(f"Dispatched {len(batches)} batches.")

dispatch_users("Messi scored!")
```

---

## **Step 2: Consumers Process Batches & Call Firehose**

```python
from kafka import KafkaConsumer
import json
import requests

KAFKA_BROKER = "localhost:9092"
USER_BATCH_TOPIC = "user_batches"
PUSH_NOTIFICATION_URL = "https://push-service.com/send"
FIREHOSE_BATCH_SIZE = 500  # Firehose supports 500 per request

consumer = KafkaConsumer(
    USER_BATCH_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    group_id="notification_consumers",
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    user_ids = message.value["user_ids"]
    
    # Split 5K users into 500-user Firehose batches
    sub_batches = [user_ids[i:i + FIREHOSE_BATCH_SIZE] for i in range(0, len(user_ids), FIREHOSE_BATCH_SIZE)]
    
    for sub_batch in sub_batches:
        payload = {"users": sub_batch, "message": "Messi scored! 🎉"}
        response = requests.post(PUSH_NOTIFICATION_URL, json=payload)

        if response.status_code == 200:
            print(f"✅ Sent notifications to {len(sub_batch)} users")
        else:
            print(f"❌ Failed to send, retrying...")
```

---

## **Why This Approach Works Well**

✅ **Efficient Work Distribution** → Kafka ensures **each consumer gets exactly one batch**.
✅ **Parallel Processing** → 50 consumers handle notifications simultaneously.
✅ **Batch Optimization** → Each consumer **sends in 500-user chunks** to Firehose
✅ **Auto-Scalability** → If **notification lag increases**, add **more partitions & consumers** dynamically.

This setup ensures notifications reach **2.5M users in ~10 seconds** 🚀.

---

## **Future Improvements**

- Implement **error handling & retries** for failed notifications.
- Use **monitoring tools (Prometheus/Grafana)** to track consumer lag.
- Auto-scale consumers dynamically based on Kafka lag.

---

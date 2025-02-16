# Infra Deep Dives

## Queues

### Kafka
#### Definition

Kafka is a distributed, fault-tolerant, high-throughput streaming platform. It's used for building real-time data pipelines and streaming applications. Think of it as a distributed commit log.
#### Components

*   **Brokers:** Servers that make up the Kafka cluster. They store topic partitions.
*   **Topics:** Categories or feeds to which messages are published.  Divided into partitions.  A **topic has 1:many relationship with partitions.** Topics are a logical abstraction.
*   **Partitions:**  Ordered, immutable sequence of records.  Enable parallelism.  Each record within a partition gets an incremental id, called offset. **Multiple partitions can reside on a single broker. A broker can have partitions from many different topics. Brokers have a many:many relationship with partitions, and a many:many relationship with topics.** Partitions are the physical unit of parallelism and storage within a Kafka cluster. Data is physically stored within partitions.
*   **Producers:** ==Applications== that publish (write) data to Kafka topics.
*   **Consumers:** ==Applications== that subscribe to (read) data from Kafka topics.
*   **Zookeeper:** (Historically) Used for managing the cluster state, broker metadata, and configuration.  Becoming less critical as Kafka evolves.
*   **Kafka Connect:** A framework for connecting Kafka with external systems (databases, file systems, etc.).
*   **Kafka Streams:** A client library for building stream processing applications on top of Kafka.

#### Important Points
1. Distribution of messages depends on partition key — meaning, each message goes to a particular partition (could be round robin or could be based on a user_id or other key)
2. **1 consumer is assigned to 1 partition**
	1. Example, if there are 10M messages per topic, spread across 10 partitions, then only 10 consumers can be assigned. 
3. **Hot partition (more applicable on write to partition rather than reads)**
	2. If one of the keys are having a LOT of messages, it will be written to a same partition, meaning, that partition becomes a HOT partition
	3. This leads to **lag** on reads, because one consumer can only do so much sequentially (you can read parallel)
	4. What to do? 
		1. Read messages in batches, and put into a separate queue for async processing, and mark as processed, as this will speed up at least the reading. Processing can be done later
		2. Back Pressure — just have producer logic to write or slowdown if there's a lag
		3. AVOID this — Prevention better than cure
			1. By using a good partition key. In this case, 
				1. Order maintain — If ordering is needed, then can't do much other than async processing. Or reconsider business logic to avoid ordering or make it stateful. Can also vertical scale. Ordering actually hinders horizontal scle
				2. No Order — just append random_id to the user_id and spread it out. If you don't need even distribution, instead want split by 3, then just append 0, 1 or 2 to the id ex: `user_id_123_0, user_id_123_1` to split to 3 partitions.
4. Retry Logic
	1. One thing to remember is that kafka doesn't have retry logic. So consumer has to handle retries — meaning, have separate topics
		1. Main Topic — for 1st time processing
		2. Retry Topic — for retries
		3. DLQ Topic — for perma fails
5. Replication
	1. If there are 5 brokers, and replication factor is 3, that means a partition is replicated across 3 different brokers. 
	2. there's only one leader "broker" at a time. So if it goes down, another is elected as a leader

###### Capacity
- A single broker can have upto 1TB of memory, and can handle 100k to 1M writes per second
- But that does not mean that consumers can consume that that scale 
###### Continuation
- Read [Notification System Using Kafka](use_case_notification_2.5_million_users.md) — This is very important
- Read [HelloInterview](https://www.hellointerview.com/learn/system-design/deep-dives/kafka) last parts for fault tolerance and scaling
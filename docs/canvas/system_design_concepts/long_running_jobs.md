#### Queues
- Slow Queues
- Fast Queues
- DLQ

#### Jobs
- store in db with states — PENDING | COMPLETED | FAILED

#### Job Stages
- Enqueue to next stage before writing to db
	- ensures that subsequent stages are not orphaned on db failures
- Make each stage `idempotent`

#### Workers
- different capacities 
- health check constantly
- **scale based on Queue Backlog**
	- Solution is called handling backpressure
	- Reject the messages if scaling is not possible
	- Accept the message while adding more workers
		- But adding more workers doesn't work for Kafka because 1:1 partition - worker
		- For kafka, adding dynamic partition is not possible

#### Handling Issues in Kafka
##### Issues
- **Consumer Lag** — workers are processing messages that's slowing them down
	- Use pause / resume to slow down
	- This will reduce in-memory load and processes the in-flight messages
	- Frees up resources
- **Queue Length** — size of the queue keeps growing
	- Reactive Solutions
		- make consumers process messages in batches 
		- make consumers use multi-threading for I/O operations
	- Proactive Solutions
		- Try to avoid this situation completely
			- By monitoring lag
			- Auto scaling workers with better capacity
			- Having large enough partitions from the beginning, so that workers can be added
# Key Points For System Design Interview

## Breakdown
The following is a very rough guide on distributing your time in a 45-minute interview session. Please remember this is a rough estimate, and the actual time distribution depends on the scope of the problem and the requirements from the interviewer.

| Step   | Description                                       | Estimated Time  |
| ------ | ------------------------------------------------- | --------------- |
| Step 1 | Understand the problem and establish design scope | 3 - 10 minutes  |
| Step 2 | Propose high-level design and get buy-in          | 10 - 15 minutes |
| Step 3 | Design deep dive                                  | 10 - 25 minutes |
| Step 4 | Wrap                                              | 3 - 5 minutes   |
|        |                                                   |                 |
### What I have missed in the past?
- Requirements
	- didn't talk about size of the data
	- didn't ask about regions — global or just USA (impacts sharding)
	- sharded at the time of writes (hot key), but didn't shard the aggregated counter table

### High Level Template (from chatgpt)
#### Step 1: Functional & Non-Functional Requirements (5 minutes)
Quickly identify the key goals and constraints of the system.
- Functional
- Non Functional (CELS)
	- **CAP Theorem**
		- for availability mention 4 9s
	- **Environmental** — device constraints, location constraints
	- **Latency** — api, sync vs async
	- **Scalability** —  bursty traffic, time of the day, read vs write ratio
	- **Size** — this migth be something important to estimate for scale
	- Durability — is loss acceptable? ex: analytic events vs payments
	- Security — access control, compliance, data isolation
	- Fault Tolerance — redundancy, failover & recovery mechanism
> [!tip] Capacity Estimation
> Important to call out to the interviewer that you would like to skip on estimations upfront and that you will do math while designing when/if necessary
#### Step 2: Core Entities & API Design (5 minutes)
Lay out the system’s main components and how they interact. Entities that your API will exchange. Call out that it's first draft. Why not list the entire data model at this point? Because you don't know what you don't know. API design should be fast enough. Focus on 
- Core Entities
- API Type — REST, GraphQL, Wire protocol
- Pagination attributes
- GET, PUT, POST, DELETE
- Idempotency

#### Step 3: High Level Design (10 - 15 minutes)
- White drawing boxes, talk about data flow
- Call out caches and message queues
- Layout table attributes 
	- Only the important ones, and call that out
	- Callout DB type — SQL vs NoSQL
- **Keep the boxes spaced out, so that you can easily introduce something new**

#### Step 4: Deep Dives (10 - 15 mins)
- meet all non functional requirements
- address edge cases
- improve design based on probes from your interviewer
- **Idempotency** and **Reliability** should be top priority
- Scalability
	- Vertical vs Horizontal scaling
	- Service — num. of hosts, host mem/cpu
	- DB — sharding, read replica, caching
	- API — rate limiting, auto scaling
	- Monitoring — service, db, mem/cpu, profiling for mem leaks, business vs. platform alerts, latency trends (p50, p90, p99)
- Error Handling
- Security — data encryption at rest, API auth, API signatures, data isolation, access controls

Question
```
Problem setup
Suppose you can import a library defining a batched_sample function, generating text using a large language model. It must be run on a pricey GPU instance on a cloud provider.

batched_sample takes in a "batch" of strings because there's an irreducible fixed latency to running any inputs, so it always takes about 100ms for the function to return regardless of the number of items in the batch. It supports batches of size 1-100 strings, and each GPU instance can only handle one batch at a time.

You can see the signature below

def batched_sample(batched_inputs: List[str]) -> List[str]:
    """
    Given a list of strings (prompts), samples a completion
    for each string and returns the new completions in a list.

    Supports batches of 1-100 input strings; latency is about 100ms
    for any batch size. Will raise an error on larger batch size.

    This function can only be run on a pricey GPU server,
    and it fully occupies the GPU on the server while it is running.
    """
    ...
Example usage of the raw function below

batched_sample([
	"E equals ",
	"For every action, there is "	
])

# Returns the following
[
	"MC squared",
	"an equal and opposite reaction"	
]
Your task
In this interview, you will design an HTTP API that exposes the above function to allow users to sample from large language models.

Users want to be able to make single requests that look like the following

curl language-model-api.anthropic.com/sample -d "E equals "
# Returns the following
#   MC squared

Requirements
- batch API takes 100 items
- we want to serv 20,000 RPS
- we want to have 500ms max latency of response
- the API is required to be strictly synchronous API
- the ordering of messages isn't required
- Total GPU needed?
```


Solution
prompt_service
- horizontal scalable
- takes requests and generates request_id (random id)
- checks batch_load_balancer on active partitions and enqueues to prompt_queue 
- polls redis cache for request_id for response
- after 500 ms, times out

prompt_queue
- kafka queue
- partitioned by req_id, makes it even distribution across number of partitions
- number of partitions equals number of batch_workers

batch_workers
- group of kafka consumers
- reads 100 messages at a time, or until queue is empty
- calls GPU batch API to execute req
- for each req_id, publishes to redis KV store

batch_load_balancer
- monitors the throughput for each worker. Since the load is balanced, each worker's batch size would be around the same, which is 100 at peak traffic, and less otherwise
- if batch size for each worker on avg is less than 100 for over a period of time, that means they're over provisioned
- maintains a partition mapping which indicates producers whihch partitions are active, and which ones are disabled.
- if, say avg batchsize is at 90, and there are 25 workers, then it's processing at the rate of 225k rps. Which means it's overprovidsiond by 2.5 which is 2.5 servers. We can disable any two of 25 partitions, and 2 workers corresponding to those partitions will be idle, and hence they can be decomissioned. 
- this way we can scale up or down.

Conclusion
- total GPU needed 20-25
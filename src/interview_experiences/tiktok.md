```python
"""
there are n machines and a list of jobs with jobs[i] = [start_i, end_i) time intervals All start_i are unique the jobs are picked as follows 

- jobs with least start time are picked first 
- a machine iwth lower id will always pick the job if more machines are available 
- a machine is busy until it finishes the job but other machines can pick up the next job if they're available 
- ex: n = 2 jobs = [[0,10],[1,5],[3,4],[2,7]] 
- answer: 0 
- 1 ➙ 0: 0, 10 
- 2 ➙ 1: 1, 5 
- 3 ➙ no op 
- 4 ➙ no op 
- 5 ➙ 1: 2, 7 (but instead of 7, it would finish at 10 because it was delayed by 3 seconds) so 5 ➙ 1: 5, 10 
- 6, 7, 8, 9 ➙ no op 
- 10 ➙ 0: 10, 11 (3, 4 was picked up) 
"""


import heapq
from collections import defaultdict

def most_active_machine(n, jobs):
    # Step 1: Sort jobs by start time
    jobs.sort()

    # Step 2: Initialize heaps and job count tracker
    available = list(range(n))  # All machines initially available
    heapq.heapify(available)

    busy = []  # (end_time, machine_id)
    job_counts = [0] * n

    for start, end in jobs:
        duration = end - start

        # Free up machines that have completed jobs by 'start'
        while busy and busy[0][0] <= start:
            freed_time, machine_id = heapq.heappop(busy)
            heapq.heappush(available, machine_id)

        if available:
            # Assign to the lowest ID available machine
            machine_id = heapq.heappop(available)
            actual_start = start
        else:
            # Wait for the earliest machine to be free
            freed_time, machine_id = heapq.heappop(busy)
            actual_start = freed_time  # Delayed start

        # Schedule job completion
        actual_end = actual_start + duration
        heapq.heappush(busy, (actual_end, machine_id))
        job_counts[machine_id] += 1

    # Step 3: Return machine with max jobs (prefer lower ID on tie)
    max_jobs = max(job_counts)
    for i, count in enumerate(job_counts):
        if count == max_jobs:
            return i

```



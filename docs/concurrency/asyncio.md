
```python
import asyncio
import time
import random
s = time.time()
# Simulate some work that takes time
async def level_d(id):
    wait_time = random.randint(1,3)
    print(f"Level D start {id} and waiting {wait_time} s")
    await asyncio.sleep(wait_time)  # Simulating I/O
    print(f"Level D end {id}")

async def level_c(id):
    print(f"Level C start {id}")

    await level_d(id)
    #wait_time = random.randint(1,3)
    #print(f"Level C wating {id} , for {wait_time} s")
    #await asyncio.sleep(wait_time)
    print(f"Level C end {id}")

async def level_b(id):
    print(f"Level B start {id}")
    await level_c(id)
    print(f"Level B end {id}")

async def level_a(id):
    print(f"Level A start {id}")
    await level_b(id)
    print(f"Level A end {id}")

# Running all tasks concurrently
async def main():
    await asyncio.gather(
        level_a(1),
        level_a(2),
        level_a(3)
    )
    e = time.time()
    print(f'Total secs = {int(e - s)}')

# Run the event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())


```





## Thread Safe Queue Simulation with Producers & Consumers
```python
from collections import deque
import random
import asyncio

class TSQ:
    def __init__(self, max_size):
        self._q = deque()
        self._max_size = max_size
        self._lock = asyncio.Lock()

    async def add(self, value):
        async with self._lock:
            if len(self._q) < self._max_size:
                self._q.append(value)
                print(len(self._q), self._q)
                #print(f"[Producer] Added {value}. Queue size: {len(self._q)}")

    async def get(self):
        async with self._lock:
            if self._q:
                item = self._q.popleft()
                #print(f"[Consumer] Processed {item}. Queue size: {len(self._q)}")
                print(len(self._q), self._q)
                return item
            else:
                return None

async def producer(tq: TSQ):
    while True:
        rand_value = random.randint(1, 10)
        await tq.add(rand_value)

        await asyncio.sleep(random.randint(0, 3))  # producers are fast

async def consumer(tq: TSQ):
    while True:
        item = await tq.get()
        if item is not None:
            await asyncio.sleep(random.randint(0, 4))  # simulate slow processing
        else:
            await asyncio.sleep(0.2)  # nothing to process, wait a bit

async def main():
    tq = TSQ(50)  # max queue size = 50

    # Start multiple producers and consumers
    producers = [asyncio.create_task(producer(tq)) for _ in range(2)]
    consumers = [asyncio.create_task(consumer(tq)) for _ in range(2)]

    await asyncio.gather(*producers, *consumers)

if __name__ == "__main__":
    asyncio.run(main())
```


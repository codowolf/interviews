
# Python Threading Module

## threading.Lock
```python
import threading
import time

shared_resource = 0
lock = threading.Lock()

def increment_resource():
    global shared_resource
    for _ in range(100000):
        # Chef wants to enter the spice pantry
        lock.acquire()
        try:
            current_val = shared_resource
            # Simulate some work or context switch possibility
            # time.sleep(0.0000001) # Even a tiny sleep can show issues without lock
            shared_resource = current_val + 1
        finally:
            # Chef leaves the pantry, MUST return the key
            lock.release()

# Without lock, shared_resource would likely be less than 200000 due to race conditions
# With lock, it will be exactly 200000

threads = []
for i in range(5): # 5 chefs
    thread = threading.Thread(target=increment_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final shared resource value: {shared_resource}") # Expected: 500000
```

You can also use `with lock:`
```python
# ...
def increment_resource_with_context_manager():
    global shared_resource
    for _ in range(100000):
        with lock: # Automatically calls acquire() at start, release() at end/exception
            current_val = shared_resource
            shared_resource = current_val + 1
# ...
```
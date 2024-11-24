<<<<<<< HEAD:Chapter-1/parallelism&multiprocessing.py
from concurrent.futures import ThreadPoolExecutor
import time

def task_1():
    # Perform addition of two numbers
    result = 5 + 3
    print("Task 1 is executed: 5 + 3 =", result)
    return result

def task_2():
    # Perform subtraction of two numbers
    result = 10 - 4
    print("Task 2 is executed: 10 - 4 =", result)
    return result

start_time = time.time()  # Start timing

with ThreadPoolExecutor() as executor:
    future1 = executor.submit(task_1)
    future2 = executor.submit(task_2)

    # Wait for the tasks to complete and retrieve results
    result1 = future1.result()
    result2 = future2.result()

end_time = time.time()  # End timing
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")
=======
]import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

# Function to add a slice of the vectors
def vector_add_slice(start, end, a, b, c):
    c[start:end] = a[start:end] + b[start:end]

# Host code
N = 1000000
a = np.random.random(N).astype(np.float32)
b = np.random.random(N).astype(np.float32)
c = np.empty(N, dtype=np.float32)

# Define the number of threads
threads = 8  # Adjust based on your system's cores
chunk_size = N // threads

# Start timing
start_time = time.time()

# Using ThreadPoolExecutor for parallelism
with ThreadPoolExecutor(max_workers=threads) as executor:
    futures = []
    for i in range(threads):
        start = i * chunk_size
        end = N if i == threads - 1 else (i + 1) * chunk_size
        futures.append(executor.submit(vector_add_slice, start, end, a, b, c))

    # Wait for all threads to finish
    for future in futures:
        future.result()

# End timing
end_time = time.time()

# Print time taken
print(f"Time taken for parallel computation: {end_time - start_time:.5f} seconds")

# Verify result and print the first 10 elements
np.testing.assert_almost_equal(c, a + b)
print(f"First 10 elements of result: {c[:10]}")
>>>>>>> e6cf681f8875d38de88da3845028b710ce4553d9:Chapter-1/Task-parallelism.py

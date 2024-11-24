import numpy as np
import time

N = 1000000

a = np.random.random(N).astype(np.float32)
b = np.random.random(N).astype(np.float32)

start_time = time.time()
c = a + b  # NumPy takes care of parallelism internally
end_time = time.time()

# Print time taken and the first 10 elements of the result
print(f"Time taken for data parallel computation (NumPy): {end_time - start_time:.5f} seconds")
print(f"First 10 elements of result: {c[:10]}")

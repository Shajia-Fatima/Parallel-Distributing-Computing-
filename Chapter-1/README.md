
# CHAPTER-1.
  # TOPICS  
# 1.Data Parallelism
This code generates two arrays of random floating-point numbers using NumPy, each with 1,000,000 elements. It performs element-wise addition of these arrays, leveraging NumPy's efficient internal parallelism. Finally, it measures and prints the computation time and the first 10 elements of the result.

# 2.Message passing programming 
This MPI-based Python code demonstrates inter-process communication using mpi4py. It requires at least two processes: process 0 sends a dictionary containing personal data to process 1, while process 1 receives and prints it. Additional processes remain idle without performing any operations.

# 3.Semaphore
This Python program uses a semaphore to synchronize access to a shared resource among multiple threads. Only one thread can access the resource at a time, ensuring thread-safe execution. It creates and starts 5 threads, each acquiring the semaphore, accessing the resource, and releasing the semaphore after a 2-second simulated task.

# 4.Serial&parallel
This Python program demonstrates concurrent execution using ThreadPoolExecutor. Two tasks (task_1 and task_2) are defined and submitted to the executor, which executes them in separate threads. The tasks print messages when executed. The with statement ensures proper resource management by automatically shutting down the thread pool.

# 5.multiprocessing
This code compares the performance of multiprocessing and multithreading for a task that processes a list using the `do_something` function (imported externally). 
   1. Multiprocessing: It spawns 10 processes, each running `do_something` with a large input size, and measures the total execution time.
   2. Multithreading: It then creates 10 threads, similarly executing `do_something`, and measures the execution time.
   3. The goal is to demonstrate the difference in execution times between multiprocessing (ideal for CPU-bound tasks) and multithreading (better for I/O-bound tasks).
      
# 6.numba-cuda
This code demonstrates GPU-based parallel computing using Numba's CUDA support. Here's a summary:
    1.GPU Kernel Definition: The vector_add function performs element-wise addition of two vectors on the GPU. Each thread processes a specific index using cuda.grid(1).
    2.Setup and Execution: It generates two random arrays (a and b) on the host (CPU), and prepares an empty array (c) for the result. The computation is distributed across GPU threads and 
       blocks, defined by threads_per_block and blocks_per_grid.
    3.Validation: After the GPU computation, the result is verified against NumPy's CPU-based addition to ensure correctness. If successful, it prints "GPU computation successful!"

# 7.Multiprocess&parallelism
# 8.process&multiprocessing
# 9.process&queue
# 10.threading 


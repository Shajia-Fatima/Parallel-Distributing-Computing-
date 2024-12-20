
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
    1. GPU Kernel Definition: The vector_add function performs element-wise addition of two vectors on the GPU. Each thread processes a specific index using cuda.grid(1).
    2.Setup and Execution: It generates two random arrays (a and b) on the host (CPU), and prepares an empty array (c) for the result. The computation is distributed across GPU threads and 
       blocks, defined by threads_per_block and blocks_per_grid.
    3.Validation: After the GPU computation, the result is verified against NumPy's CPU-based addition to ensure correctness. If successful, it prints "GPU computation successful!"

# 7.Multiprocess&parallelism
This code performs parallel element-wise addition of two large arrays using Python's ThreadPoolExecutor. The arrays are divided into slices, and each slice is processed by a separate thread. The computation time is measured, the result is verified for correctness, and the first 10 elements of the output are printed.

# 8.process&multiprocessing
This code demonstrates the use of Python's multiprocessing module to run two separate processes concurrently.
Processes: It creates two processes: one for printing the square of a number and another for printing the cube.
Start and Join: The processes are started using start(), and join() is used to ensure the main program waits for both processes to complete before printing "Processes finished executing".
Execution: The square and cube calculations for the number 10 are done in parallel.

# 9.process&queue
This code demonstrates producer-consumer interaction using Python's `multiprocessing` module. The producer generates data and puts it in a shared queue, while the consumer retrieves and processes the data. The processes are synchronized using `join()` to ensure they complete before the program finishes.

# 10.threading 
This code demonstrates the use of multithreading to compute the Fibonacci sequence. Here's a brief summary:
Fibonacci Calculation: The function calc_fibonacci recursively calculates the Fibonacci number for a given n.
Multithreading: Four threads are created, each running the calc_fibonacci function with an argument of 30. The threads start concurrently and each begins the Fibonacci calculation.
Synchronization: join() ensures the main program waits for all threads to complete before finishing.
Note: Due to the recursive nature of calc_fibonacci, the code may run slowly for large values like 30, especially with multithreading since the calls are CPU-bound.









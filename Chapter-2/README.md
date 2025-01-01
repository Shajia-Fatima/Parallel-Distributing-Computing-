# Chapter 2:
 # Topics Covered:
# Barrier
This code simulates a race where multiple threads (representing runners) reach a barrier before proceeding. Here's a summary:
   1. Barrier Synchronization: A `Barrier` is used to synchronize the runners. Each runner (thread) waits at the barrier until all runners have reached it.
   2. Runners: Three runners (`Huey`, `Dewey`, and `Louie`) are simulated by threads. Each thread sleeps for a random time between 2 and 5 seconds before reaching the barrier.
   3. Race Execution: The race begins, and once all runners reach the barrier, the race continues and finishes.
The use of `Barrier` ensures that all threads (runners) wait for each other before continuing.

# Condition
This code simulates the producer-consumer problem using threading and a `Condition` for synchronization. The producer thread adds items to a shared list, while the consumer thread removes them. Both threads wait when the list is full or empty, respectively, ensuring proper coordination. Actions are logged with timestamps for clarity, and `join()` ensures the main function waits for both threads to finish.

# Event
This code demonstrates the producer-consumer problem using Python's `threading.Event` for synchronization between two threads. The `Producer` thread generates random items and appends them to a shared list, signaling the `Consumer` thread each time an item is added by setting the event with `event.set()`. The `Consumer` thread waits for the event to be set and then pops an item from the list to consume it. The event ensures that the consumer only consumes items after they are produced, preventing race conditions. The actions of both threads are logged with timestamps and thread names, and `join()` ensures the program waits for both threads to finish before exiting.

# Thread Class
This code demonstrates the use of multiple threads to perform tasks concurrently. It defines a custom MyThreadClass that inherits from the Thread class and overrides the run() method. Each thread prints its name, the process ID, and sleeps for a randomly chosen duration between 1 and 10 seconds before completing. In the main() function, nine threads are created with random durations, started, and joined, ensuring the program waits for all threads to finish before exiting. The program also tracks and prints the total execution time, showing how long it takes to execute all threads concurrently. Each thread operates independently, but the main program ensures that all threads complete before printing "End" and displaying the total time taken.

# Thread Lock
The key difference between the two codes is in how the lock (`threadLock`) is handled and the timing of when it is acquired and released:
1. First Code (Lock before and after sleep):
   - The lock is acquired before printing the thread's name and process ID and is released right after the print statement, before the thread sleeps.
   - This ensures that only one thread can print at a time, and other threads are blocked until the lock is released.
   - The sleep operation does not hold the lock, meaning threads can potentially execute other tasks or acquire the lock once they are done sleeping.
2. Second Code (Lock only around print statement):
   - The lock is acquired only around the printing of the thread's name and process ID and is released immediately after printing.
   - After that, the thread sleeps without holding the lock, allowing other threads to run and acquire the lock while the current thread is sleeping.
   - This reduces the contention for the lock and improves efficiency since the sleep period does not block other threads from acquiring the lock and executing.
 Why the Answers Differ:
   - Concurrency Control: In the first code, the lock is held for a longer time (including while the thread is sleeping), which can reduce concurrency, as no other thread can run during that period. In the second code, the lock is only held briefly while printing, allowing better parallel execution during the sleep period, as the lock is released before the thread sleeps.
   - Efficiency: The second code is more efficient because it allows other threads to execute while one is sleeping, whereas the first code makes all threads wait until the lock is released, even when not actively executing.

In summary, the first code is more restrictive in terms of concurrency, while the second code allows for better parallelism by holding the lock for a shorter time.

# RLock
The provided code demonstrates thread synchronization using `RLock` in a `Box` class that manages a shared resource, `total_items`. Two threads are created: one for adding items to the box and the other for removing them. Both operations are performed in a thread-safe manner by acquiring the lock to ensure mutual exclusion while modifying `total_items`. The threads run concurrently, and each thread adds or removes a random number of items. The code ensures that no race conditions occur when modifying the shared resource, as the lock prevents simultaneous access by multiple threads.

# Semaphore
The provided code demonstrates producer-consumer synchronization using a `Semaphore`. The `consumer` thread waits for the semaphore to be released, while the `producer` thread generates a random item, logs it, and then releases the semaphore. The semaphore ensures that the consumer only proceeds after the producer has produced an item. The program runs 10 iterations, each with a producer and a consumer thread, and logs their actions with timestamps. This example showcases how semaphores are used to coordinate access to shared resources between threads.

# Thread Definition
The provided code creates 10 threads, each of which calls the `my_func` function with a unique thread number as an argument. The `my_func` function simply prints a message indicating which thread called it. The main function initializes and starts each thread in a loop, and the `join()` method ensures that the main thread waits for each thread to finish before starting the next one. This guarantees that each thread completes its execution in sequence.

# Thread Determine
The code creates three threads, each responsible for executing one of the functions `function_A`, `function_B`, or `function_C`. Each function prints a message when it starts and exits, with a 2-second sleep in between. The `start()` method is called to initiate each thread, and `join()` is used to ensure that the main thread waits for all threads to finish their execution before proceeding. This ensures that the functions run concurrently, and their output is printed in the order they complete.

# Thread name and processes
The code defines a custom thread class `MyThreadClass`, inheriting from `Thread`, which prints the process ID when each thread runs. Two threads (`thread1` and `thread2`) are created and started, which execute the `run()` method in parallel. The `join()` method ensures the main program waits for both threads to finish before printing "End." However, the `os.getpid()` is mentioned in a comment but isn't used in the `run()` method. The program demonstrates basic thread creation and management in Python using the `Thread` class.

# Thread with queue
The code demonstrates thread synchronization using a `Queue` in Python. It involves two main components: a `Producer` class and a `Consumer` class. The `Producer` thread generates random numbers and adds them to a shared queue, while the `Consumer` threads repeatedly retrieve and process the items from the queue. The `Queue` is used to safely share data between threads, ensuring that one thread does not modify the queue while another is using it.

The program starts one `Producer` thread and three `Consumer` threads. The `Producer` thread generates five random numbers, adds them to the queue, and notifies that an item has been added. The `Consumer` threads remove items from the queue and process them, notifying each time an item is consumed.
The `queue.task_done()` method is used by the consumers to indicate that the task (i.e., the item retrieval) has been completed. The `join()` method ensures that the main thread waits for all threads to finish before exiting.

This setup helps in managing multiple consumers working concurrently on the shared queue, making it a good example of thread synchronization.

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


# Semaphore
# Thread Definition
# Thread Determine
# Thread name and processes
# Thread with queue

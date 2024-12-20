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
This code demonstrates the use of threading with a lock to manage concurrent execution. The `MyThreadClass` creates threads that each print their name and process ID, then sleep for a random duration. A `Lock` is used to ensure that only one thread runs at a time, preventing race conditions. In the `main()` function, nine threads are created and started, then joined to ensure the main program waits for all threads to finish. The program calculates and prints the total execution time, showing how long it takes for all threads to complete their tasks sequentially due to the lock.

# RLock
This code demonstrates the use of threads with a lock to ensure controlled access to shared resources. Nine threads are created, each with a random sleep duration. The `threadLock` is acquired before printing the thread's name and process ID, then released after printing to allow other threads to run. Each thread sleeps for a random time, and the main program waits for all threads to complete using `join()`. The execution time is measured and displayed, showing how long it takes for all threads to finish their tasks, with the lock ensuring no thread interference during the print statement.

# Semaphore
# Thread Definition
# Thread Determine
# Thread name and processes
# Thread with queue

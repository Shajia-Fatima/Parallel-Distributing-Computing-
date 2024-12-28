   # CHAPTER 3
# Topics Covered:

# Spawing_a_Process:
This code demonstrates **process spawning** using Python's `multiprocessing` module, where each iteration creates a new process to execute `myFunc`. A process is an independent unit of execution with its own memory space. Here, `myFunc` prints a message and iterates from `0` to the given number `i`, printing values. The `main` function spawns and starts one process at a time with `process.start()`, and `process.join()` ensures the main program waits for the current process to finish before starting the next. This sequential execution limits parallelism, but it showcases how processes are created and managed for tasks.

# Communication_with_pipe:
This code demonstrates *inter-process communication* using **pipes** in Python's `multiprocessing` module. It creates two processes: `create_items`, which generates numbers from 0 to 9 and sends them through the first pipe (`pipe_1`), and `multiply_items`, which reads those numbers, squares them, and sends the results through the second pipe (`pipe_2`). The main process closes the unused ends of the pipes and continuously reads the squared numbers from `pipe_2`. When all data is processed, an `EOFError` indicates the end of data, and the loop exits with the message "End". The pipes serve as unidirectional communication channels, transferring data between the processes. Using `Pipe(True)` creates a duplex pipe, allowing both ends to send and receive data. This approach facilitates concurrent execution, where processes work independently while communicating efficiently via pipes to exchange data. The final output displays the squares of numbers from 0 to 9, followed by "End".

# Communication_with_queue:
This code demonstrates *inter-process communication* using a shared **queue** in Python's `multiprocessing` module, implementing the producer-consumer model. The **producer** generates 10 random integers and appends them to the shared queue, while the **consumer** retrieves and processes these items. The queue ensures thread-safe communication between the processes. The producer and consumer run independently, with the producer adding data and the consumer consuming it. The queue synchronizes access, preventing race conditions. The output shows the producer appending items and the consumer processing them, illustrating a concurrent workflow.

# Daemon:
This code demonstrates the use of **daemon** and **non-daemon processes** in Python's `multiprocessing` module. Two processes are created: a **background (daemon) process** and a **non-background (non-daemon) process**. The `foo` function, executed by both processes, prints a sequence of numbers depending on the process type. The background process runs as a daemon, meaning it can be terminated when the main program ends, even if it hasn't completed its task. The non-background process runs to completion, as it is non-daemon. The main program allows the daemon process to run briefly by adding a `time.sleep(2)` delay. The output shows both processes printing their sequences, with the daemon process potentially being interrupted if the main program ends too soon.

# Killing_processes:
# myFunct:
# Naming_processes:
# Process_Barrier:
# Process_in_subclass:
# Process_pool:
# run_background_process:
# run_background_processes_no_deamon:
# Spawing_namespaces:

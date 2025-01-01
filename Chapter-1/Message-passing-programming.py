import time
import multiprocessing
import threading

# Define the `do_something` function
def do_something(size, out_list):
    for _ in range(size):
        out_list.append(1)  # Example operation: adding elements to the list

if __name__ == "__main__":
    size = 100000
    procs = 4
    jobs = []

    # Multiprocessing
    start_time = time.time()
    for i in range(procs):
        out_list = multiprocessing.Manager().list()  # Shared list for processes
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time)

    # Reset jobs list for threading
    jobs = []
    threads = 4
    start_time = time.time()
    for k in range(threads):
        out_list = list()  # Local list for each thread
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for l in jobs:
        l.start()

    for l in jobs:
        l.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multithreading time =", end_time - start_time)

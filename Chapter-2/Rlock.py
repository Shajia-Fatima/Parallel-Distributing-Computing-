import threading
import time
import random

class Box:
    def __init__(self):
        self.lock = threading.RLock()  
        self.total_items = 0  # Initial total_items is 0

    def execute(self, value):
        with self.lock:  # Acquiring the lock
            self.total_items += value  # Modifying shared resource (total_items)

    def add(self):
        with self.lock:  # Acquiring the lock
            self.execute(1)  # Increase the total_items by 1

    def remove(self):
        with self.lock:  # Acquiring the lock
            self.execute(-1)  # Decrease the total_items by 1

def adder(box, items):
    print("N° {} items to ADD \n".format(items))
    while items:  
        box.add()
        time.sleep(1)  
        items -= 1
        print("ADDED one item -->{} item to ADD \n".format(items))

def remover(box, items):
    print("N° {} items to REMOVE \n".format(items))
    while items:  
        box.remove() 
        time.sleep(1) 
        items -= 1 
        print("REMOVED one item -->{} item to REMOVE\n".format(items))

def main():
    items = 10
    box = Box() 

    # Create two threads: one for adding items and one for removing items
    t1 = threading.Thread(target=adder, args=(box, random.randint(10,20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1,10))) 

    # Start the threads
    t1.start()
    t2.start()

    # Wait for both threads to finish before continuing
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

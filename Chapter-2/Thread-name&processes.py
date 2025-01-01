import os
from threading import Thread

class MyThreadClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
 
    def run(self):
        print(f"ID of thread running {self.name} is {os.getpid()}")

def main():
    # Thread creation
    thread1 = MyThreadClass("Thread#1")
    thread2 = MyThreadClass("Thread#2")
  
    # Thread starting
    thread1.start()
    thread2.start()

    # Thread joining
    thread1.join()
    thread2.join()

    # End
    print("End of main program.")

if __name__ == "__main__":
    main()

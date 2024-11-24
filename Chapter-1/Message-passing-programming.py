from mpi4py import MPI

# Initialize MPI communication
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Get the rank of the current process
size = comm.Get_size()  # Get the total number of processes

if size < 2:
    print("This program requires at least 2 processes.")
else:
    if rank == 0:
        # Changed the data to something different
        data_to_send = {'Name': 'Alice', 'Age': 25, 'City': 'New York'}
        comm.send(data_to_send, dest=1)
        print("Process 0: Sent data to process 1")
    elif rank == 1:
        received_data = comm.recv(source=0)  # Receive data from process 0
        print(f"Process 1: Received data - {received_data}")
    else:
        print(f"Process {rank}: No operations assigned. Remaining idle.")

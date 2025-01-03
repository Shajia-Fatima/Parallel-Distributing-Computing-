from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank

# Initialize data_received to avoid the NameError
data_received = None

if rank == 1:
    data_send = "a"
    destination_process = 2
    source_process = 2
    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)

if rank == 2:
    data_send = "b"
    destination_process = 1
    source_process = 1
    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)

# Print data_received for all processes
print(f"Process {rank} received: {data_received}")

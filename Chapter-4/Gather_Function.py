from mpi4py import MPI

# Initialize communicator, rank, and size
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Define data for each process
data = (rank + 1) ** 2

# Gather data at root process (rank 0)
data = comm.gather(data, root=0)

# Print gathered data at root
if rank == 0:
    print("rank = %s ...receiving data from other processes" % rank)
    for i in range(1, size):
        value = data[i]
        print("process %s receiving %s from process %s" % (rank, value, i))

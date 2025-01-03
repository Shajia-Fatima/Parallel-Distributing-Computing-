from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Root process prepares the data as a NumPy array
    data = np.arange(10, dtype='i')  # Create an array with 10 integers
    counts = [1, 2, 3, 4]            # Number of elements for each process
    displacements = [0, 1, 3, 6]     # Starting indices for each process
else:
    # Other processes do not have the data
    data = None
    counts = None
    displacements = None

# Broadcast counts and displacements to all processes
counts = comm.bcast(counts, root=0)
displacements = comm.bcast(displacements, root=0)

# Each process prepares a NumPy receive buffer
recvbuf = np.zeros(counts[rank], dtype='i')  # Allocate buffer based on count

# Scatter the data
comm.Scatterv([data, counts, displacements, MPI.INT], recvbuf, root=0)

print(f"Process {rank} received: {recvbuf}")

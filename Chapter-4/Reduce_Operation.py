import numpy
from mpi4py import MPI

# Initialize communicator, rank, and size
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

# Define array size and data to send
array_size = 10
senddata = (rank + 1) * numpy.arange(array_size, dtype=int)  # Use `int` instead of `numpy.int`
recvdata = numpy.zeros(array_size, dtype=int)  # Use `int` instead of `numpy.int`

# Print sending data
print("process %s sending %s" % (rank, senddata))

# Perform Reduce operation with MPI.SUM
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

# Print reduced data at root
if rank == 0:
    print("on task", rank, "after Reduce: data =", recvdata)

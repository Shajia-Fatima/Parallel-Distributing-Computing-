from mpi4py import MPI
import numpy

# Initialize communicator, rank, and size
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Define data to send and receive
senddata = (rank + 1) * numpy.arange(size, dtype=int)
recvdata = numpy.empty(size, dtype=int)

# Perform Alltoall communication
comm.Alltoall(senddata, recvdata)

# Print sent and received data
print("process %s sending %s receiving %s" % (rank, senddata, recvdata))

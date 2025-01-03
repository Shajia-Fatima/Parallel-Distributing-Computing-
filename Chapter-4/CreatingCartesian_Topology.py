from mpi4py import MPI
import numpy as np

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Initialize neighbors array
neighbour_processes = [0, 0, 0, 0]

if __name__ == "__main__":
    # Initialize communicator, rank, and size
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    # Define grid dimensions
    grid_rows = int(np.floor(np.sqrt(comm.size)))
    grid_columns = comm.size // grid_rows

    if grid_rows * grid_columns > size:
        grid_columns -= 1
    if grid_rows * grid_columns > size:
        grid_rows -= 1

    # Print grid dimensions at root
    if rank == 0:
        print("Building a %d x %d grid topology:" % (grid_rows, grid_columns))

    # Create Cartesian topology
    cartesian_communicator = comm.Create_cart(
        (grid_rows, grid_columns), periods=(False, False), reorder=True
    )

    # Get coordinates and neighbors
    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)
    neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)

    print("Process = %s row = %s column = %s --> neighbour_processes[UP] = %s "
          "neighbour_processes[DOWN] = %s neighbour_processes[LEFT] = %s "
          "neighbour_processes[RIGHT] = %s" %
          (rank, my_mpi_row, my_mpi_col, neighbour_processes[UP], neighbour_processes[DOWN],
           neighbour_processes[LEFT], neighbour_processes[RIGHT]))

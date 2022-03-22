from mpi4py import MPI
from pyrustmpi import lib, ffi

comm = MPI.COMM_WORLD
comm_ptr = MPI._addressof(comm)
comm_val = ffi.cast('MPI_Comm*', comm_ptr)[0]

lib.sayhello(comm_val)
lib.cleanup(comm_val)
from mpi4py import MPI
from pyrustmpi import ffi, sayhello

comm = MPI.COMM_WORLD
ptr = MPI._addressof(comm)
raw = ffi.cast('uintptr_t*', ptr)

sayhello(raw)
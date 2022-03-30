from mpi4py import MPI
from pyrustmpi import lib, ffi

comm = MPI.COMM_WORLD
ptr = MPI._addressof(comm)
raw = ffi.cast('uintptr_t', ptr)

lib.sayhello(raw)

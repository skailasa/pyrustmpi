from mpi4py import MPI
from .pyrustmpi import lib, ffi


sayhello = lib.sayhello

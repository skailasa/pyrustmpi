import os

from cffi import FFI
from mpi4py import MPI

HERE = os.path.abspath(os.path.dirname(__file__))
LIBDIR = os.path.join(HERE)
 
ffi = FFI()

if MPI._sizeof(MPI.Comm) == ffi.sizeof('int'):
    _mpi_comm_t = 'int'
else:
    _mpi_comm_t = 'void*'

ffi.cdef("""
typedef %(_mpi_comm_t)s MPI_Comm;
void sayhello(MPI_Comm);
void cleanup(MPI_Comm);
""" % vars()
)

lib = ffi.dlopen(os.path.join(LIBDIR,  "libpyrustmpi.so"))

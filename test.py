import os

from cffi import FFI
# from mpi4py import MPI

HERE = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(HERE, "target", "debug", "libpyrustmpi.dylib")


ffi = FFI()

ffi.cdef("""
    int initialize_mpi();
""")

C = ffi.dlopen(PATH)
u = C.initialize_mpi()
print(u)
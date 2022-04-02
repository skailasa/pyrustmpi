import numpy as np
from mpi4py import MPI
from pyrustmpi import ffi, sayhello, expose, _next, expose_mytype, MyTypeVec

# from rust_ext import mult

# comm = MPI.COMM_WORLD
# ptr = MPI._addressof(comm)
# raw = ffi.cast('uintptr_t*', ptr)

# sayhello(raw)


data_pointer = expose_mytype(10)

vec = MyTypeVec(data_pointer, 5)

for element in vec:
    print(element.x)
print()
for element in vec:
    print(element.x)

# print(vec)
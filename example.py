import numpy as np
from mpi4py import MPI
from pyrustmpi import ffi, sayhello, expose, MyTypeIter, MyType


# 1. Example of a trivial MPI function
comm = ffi.cast('uintptr_t*',MPI._addressof(MPI.COMM_WORLD))
sayhello(comm)

# 2. Example of a trivial Rust buffer exposed as a Python iterator
n = 10
head = expose(n)
vec = MyTypeIter(head, n)

for element in vec:
    # print(MyType(element))
    print((element))

print(vec)

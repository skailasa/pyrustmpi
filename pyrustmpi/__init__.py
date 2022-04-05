"""
Demo project to test out Rust/Python/MPI ideas
"""
from mpi4py import MPI
import numpy as np
from .pyrustmpi import lib, ffi

# Native functions
sayhello = lib.sayhello
expose = lib.expose

class MyType:
    """Wrapper for a custom type from Rust"""
    def __init__(self, pointer):
        self._pointer = pointer

    @property
    def ctype(self):
        return self._pointer

    @property
    def x(self):
        return self.ctype.x

    def __repr__(self):
        return 'MyType '+str({'x': self.x})


class MyTypeIter:
    """Interface for an iterator over MyType objects from Rust"""
    def __init__(self, head, n):
        self._head = head
        self._curr = self._head
        self._iter = 0
        self._n = n

    @property
    def curr(self):
        return MyType(self._curr)

    @property
    def head(self):
        return MyType(self._head)
    
    def __len__(self):
        return self._n

    def __iter__(self):
        self._curr = self._head
        self._iter = 0
        return self

    def __next__(self):
        _curr = self._curr
        _next = lib.next(self._curr)[0]

        if self._iter < len(self):
            if _curr != _next:
                self._curr = _next
                self._iter += 1
                return _curr
        else:
            raise StopIteration

    def __repr__(self):
        nslice = len(self)
        ntot = ffi.cast('size_t', len(self))
        start = ffi.cast('size_t', 0)
        stop = ffi.cast('size_t', nslice)
        ptr = np.empty(nslice, dtype=np.uint64)
        ptr_data = ffi.from_buffer('uintptr_t *', ptr)
        lib.slice(self._head, ptr_data, ntot, start, stop)
        _repr =  [MyType(ffi.cast('MyType *', ptr[index])) for index in range(nslice)]
        return str(_repr)

    def _index(self, index):
        index = ffi.cast('size_t', index)
        ntot = ffi.cast('size_t', len(self))
        ptr = lib.index(self._head, ntot, index)
        return ptr

    def _slice(self, start, stop):
        nslice = stop-start
        ptr = self._index(start)[0]
        return MyTypeIter(ptr, nslice)

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, _ = key.indices(len(self))
            return self._slice(start, stop)

        elif isinstance(key, int):
            ptr = self._slice(key, key+1)
            return ptr

        else:
            raise TypeError('Invalid argument type: {}'.format(type(key)))

    @property
    def x(self):
        return self.curr.x

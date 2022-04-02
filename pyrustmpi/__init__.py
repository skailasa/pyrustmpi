from mpi4py import MPI
import numpy as np
from .pyrustmpi import lib, ffi

sayhello = lib.sayhello
expose = lib.expose
_next = lib.next
expose_mytype = lib.expose_mytype
_next_mytype = lib.next_mytype


class MyTypeVec:

    def __init__(self, pointer, len):
        self._head = pointer
        self._curr = pointer
        self._iter = 0
        self.len = len

    @property
    def ctype(self):
        return self._head

    def __len__(self):
        return self.len

    def __iter__(self):
        self._curr = self._head
        self._iter = 0
        return self

    def __next__(self):
        _curr = self._curr
        _iter = self._iter
        _next = lib.next_mytype(self._curr)[0]

        if _iter < self.len:
            if _curr != _next:
                self._curr = _next
                self._iter += 1
                return _curr
        else:
            raise StopIteration

    @property
    def x(self):
        return self._curr.x

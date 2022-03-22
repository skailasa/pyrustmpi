from mpi4py import MPI
import hello as hw

comm = MPI.COMM_WORLD

comm_ptr = MPI._addressof(comm)
comm_val = hw.ffi.cast('MPI_Comm*', comm_ptr)[0]
hw.lib.sayhello(comm_val)
hw.lib.cleanup(comm_val)


try:
    hw.sayhello(list())
except:
    pass
else:
    assert 0, "exception not raised"
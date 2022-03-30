use mpi::traits::*;
use mpi::topology::UserCommunicator;

use mpi::ffi::{MPI_Comm};

#[no_mangle]
pub extern "C" fn sayhello(comm: *mut usize) {
    let comm = std::mem::ManuallyDrop::new(unsafe {UserCommunicator::from_raw(*comm as MPI_Comm)}.unwrap());
    let rank = comm.rank();
    println!("Hello from {:?}", rank);
}

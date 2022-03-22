use mpi::traits::*;
use mpi::topology::UserCommunicator;

use mpi::ffi::{MPI_Comm, MPI_Comm_free};

#[no_mangle]
pub extern "C" fn sayhello(comm: MPI_Comm) {
    let comm = std::mem::ManuallyDrop::new(unsafe {UserCommunicator::from_raw(comm)}.unwrap());
    let rank = comm.rank();
    println!("Hello from {:?}", rank);
}

#[no_mangle]
pub extern "C" fn cleanup(comm: &mut MPI_Comm) 
{
    unsafe {MPI_Comm_free(comm)};
}

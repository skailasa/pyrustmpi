use mpi::traits::*;
use mpi::topology::UserCommunicator;
use mpi::ffi::{MPI_Comm};

/// Trivial MPI function
#[no_mangle]
pub extern "C" fn sayhello(comm: *mut usize) {
    let comm = std::mem::ManuallyDrop::new(unsafe {UserCommunicator::from_raw(*comm as MPI_Comm)}.unwrap());
    let rank = comm.rank();
    println!("Hello from {:?}", rank);
}



/// Simple struct with a single element
#[repr(C)]
#[derive(Clone, Copy, Debug, Default)]
pub struct MyType{pub x: u32}


/// Test function to expose an iterator via a raw pointer to its head
#[no_mangle]
pub extern "C" fn expose(n: usize) -> *mut MyType {

    let mut arr: Vec<MyType> = Vec::new();

    for i in 0..n {
        arr.push(MyType{x: i as u32})
    }

    arr.as_mut_ptr()
}

/// Next element of a vector exposed via a raw pointer
#[no_mangle]
pub extern "C" fn next(ptr: *const MyType) -> *mut &'static MyType {
    let mut slice = unsafe {std::slice::from_raw_parts(ptr, 2).iter()};
    let _ = slice.next();
    let next = slice.next().unwrap();
    Box::into_raw(Box::new(next))
}


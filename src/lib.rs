use mpi::traits::*;
use mpi::topology::UserCommunicator;
use mpi::ffi::{MPI_Comm};

#[no_mangle]
pub extern "C" fn sayhello(comm: *mut usize) {
    let comm = std::mem::ManuallyDrop::new(unsafe {UserCommunicator::from_raw(*comm as MPI_Comm)}.unwrap());
    let rank = comm.rank();
    println!("Hello from {:?}", rank);
}


#[repr(C)]
#[derive(Clone, Copy, Debug, Default)]
pub struct MyType{pub x: u32}


#[no_mangle]
pub extern "C" fn expose(n: usize) -> *mut u32 {

    let mut arr: Vec<u32> = vec![1, 2, 3, 4, 5];

    arr.as_mut_ptr()
}

#[no_mangle]
pub extern "C" fn expose_mytype(n: usize) -> *mut MyType {

    let mut arr: Vec<MyType> = vec![MyType{x: 1}, MyType{x: 2}, MyType{x: 3}, MyType{x: 4}, MyType{x: 5}];

    arr.as_mut_ptr()
}

#[no_mangle]
pub extern "C" fn next(ptr: *const u32) -> *mut &'static u32 {
    
    let mut slice = unsafe {std::slice::from_raw_parts(ptr, 1).iter()};
    let next = slice.next();
    let nextnext = slice.next().unwrap();
    Box::into_raw(Box::new(nextnext))
}

#[no_mangle]
pub extern "C" fn next_mytype(ptr: *const MyType) -> *mut &'static MyType {
    
    let mut slice = unsafe {std::slice::from_raw_parts(ptr, 2).iter()};
    let _ = slice.next();
    let next = slice.next().unwrap();
    Box::into_raw(Box::new(next))

}



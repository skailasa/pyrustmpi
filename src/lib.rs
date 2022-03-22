use mpi::traits::*;
use mpi::environment::Universe;

#[no_mangle]
pub extern "C" fn initialize_mpi() -> *mut Universe {

        let universe = mpi::initialize().unwrap();
        let universe = Box::new(universe);
        Box::into_raw(universe)
}

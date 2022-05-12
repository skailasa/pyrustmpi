# PyRustMPI

Minimal example of Python + Rust + MPI project for Linux projects. Relies on a working MPI installation being available on your system.

## Build From Source

Install maturin crate

```bash
cargo install maturin
```

Maturin automatically creates dynamic library as well as all headers in a platform agnostic way.

```bash
maturin build . && python -m pip install .
```

Release mode

```bash
maturin build . --release && python -m pip install .
```

## Install Built Python Package From Anaconda

Linux/MacOS packages available from Anaconda Cloud into a Conda environment.

```bash
conda install -c skailasa pyrustmpi
```

Install mpi4py dependency separately, to ensure that correct pointers are
created to shared libraries when installing into a virtual environment

```
env MPICC=/path/to/mpicc python -m pip install mpi4py
```

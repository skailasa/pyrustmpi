[![Anaconda-Server Badge](https://anaconda.org/skailasa/pyrustmpi/badges/platforms.svg)](https://anaconda.org/skailasa/pyrustmpi)

[![Anaconda-Server Badge](https://anaconda.org/skailasa/pyrustmpi/badges/version.svg)](https://anaconda.org/skailasa/pyrustmpi)


# PyRustMPI

Minimal example of Python + Rust + MPI project for Mac and Linux projects.


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

### Notes

Installation requires that your channel list contains `conda-forge`.

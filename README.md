[![Anaconda-Server Badge](https://anaconda.org/skailasa/pyrustmpi/badges/platforms.svg)](https://anaconda.org/skailasa/pyrustmpi)

[![Anaconda-Server Badge](https://anaconda.org/skailasa/pyrustmpi/badges/version.svg)](https://anaconda.org/skailasa/pyrustmpi)


# PyRustMPI

Minimal example of Python + Rust + MPI project for Mac and Linux projects.


## Build

Using Conda Build to generate a Conda package

```bash
conda build conda.recipe
```

Alternatively, build from within a virtual environment manually.

```bash
# Create a virtulenv called 'build'
conda env create -f environment.yaml && conda activate build

# Build just Rust package with Cargo
cargo build

# Build combined Rust and Python package with Maturin
maturin build
```

## Install

Install from Anaconda Cloud into a Conda environment.

```bash
conda install -c skailasa pyrustmpi
```

Install mpi4py dependency separately, to ensure that correct pointers are
created to shared libraries when installing into a virtual environment

```
env MPICC=/path/to/mpicc python -m pip install mpi4py
```

**Installation requires that your channel list contains `conda-forge`.**

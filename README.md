# PyRustMPI

Minimal example of Python + Rust + MPI project for Linux projects. Relies on a working MPI installation being available on your system.

## Install

Install pre-built Python wheel from PyPI

```bash
pip install -r requirements && pip install pyrustmpi
```

## Build

```bash
# Fresh Python build environment
conda create -n build_env python=3.8 && conda activate  build_env

# Install package dependencies
pip install -r requirements.txt

# Build Rust library and copy into Python package
cargo build --release && \
cp target/release/libpyrustmpi.so python/pyrustmpi/

# Build Python wheel
cd python &&  \
python setup.py bdist_wheel --plat-name=manylinux1_x86_64 \

# Upload to PyPI.
twine upload dist/pyrustmpi-<VERSION_NUMBER>-py3-none-manylinux1_x86_64.whl 
```

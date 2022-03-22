# PyRustMPI

Minimal example of Python + Rust + MPI project for Linux projects. Relies on a working MPI installation being available on your system.

## Install

Install pre-built Python wheel from PyPI

```bash
pip install -r requirements.txt && pip install pyrustmpi
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

## Gotchas

I'm not totally happy with this project structure.

Things I need to understand better:

- What's the best way of distributing a dynamic library for use in a Python project? This works, but seems like a hack.
- I'd preferably want to distribute using Conda, how do I do that?
- How can I build this on Mac, where rsmpi's GCC stuff seems to fail?

Notes:

- RSMPI calls Drop on Communicators at the end of the Rust function, so have to manually manage this memory from Python.
- Lose quite a lot of information in using C ABI, have to find a way to wrap functions to keep documentation clear.
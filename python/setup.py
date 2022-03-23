from setuptools import setup

# Build requirements
requirements = []

setup(
    name='pyrustmpi',
    version='0.0.6',
    descripion='Python Bindings for a Rust MPI application',
    packages=['pyrustmpi'],
    package_data={
        'pyrustmpi': ['libpyrustmpi.so']
    },
    zip_safe=False,
)
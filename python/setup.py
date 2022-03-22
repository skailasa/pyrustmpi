from setuptools import setup, Distribution


setup(
    name='pyrustmpi',
    version='0.0.6',
    descripion='Python Bindings for a Rust MPI application',
    packages=['pyrustmpi'],
    package_data={
        'pyrustmpi': ['libpyrustmpi.so']
    }
)
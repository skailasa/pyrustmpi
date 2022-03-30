# PyRustMPI

Minimal example of Python + Rust + MPI project for Linux projects. Relies on a working MPI installation being available on your system.

# Build using Maturin

Install maturin crate

```bash
cargo install maturin
```

Maturin automatically creates dynamic library as well as all headers in a platform agnostic way.

```bash
maturin develop
```

Release mode

```bash
maturin develop --release
```



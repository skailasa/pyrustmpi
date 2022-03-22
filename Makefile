install:
	pip install -r requirements.txt

build: src pyrustmpi
	cargo build --release
	cp target/release/libpyrustmpi.so python/pyrustmpi/libpyrustmpi.so
	cd python; python setup.py bdist_wheel --plat-name=manylinux1_x86_64

upload: pyrustmpi dist build 
	cd python; twine upload dist/pyrustmpi-0.0.6-py3-none-manylinux1_x86_64.whl 
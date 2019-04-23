.PHONY: all build test clean

all: clean build test

build:
	python setup.py build_ext -i

test:
	python test.py

clean:
	rm -f *so _*cpp 
	rm -rf build/*

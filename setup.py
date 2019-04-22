from distutils.core import setup, Extension
import numpy
from Cython.Distutils import build_ext
from Cython.Build import cythonize

setup(
        name='cross_correlation', 
        ext_modules=cythonize('cross_correlation.pyx')
        )

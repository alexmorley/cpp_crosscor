from distutils.core import setup, Extension
import numpy
from Cython.Distutils import build_ext
from Cython.Build import cythonize

extensions = [
        Extension("cross_correlation", ["cross_correlation.pyx"],
            include_dirs=[numpy.get_include()])
        ]

setup(
        name='cross_correlation', 
        #ext_modules=cythonize('cross_correlation.pyx', include_path = [numpy.get_include()]
        ext_modules=cythonize(extensions)
        )

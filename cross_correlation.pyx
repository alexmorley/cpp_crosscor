# distutils: language = c++

# cimport the Cython declarations for numpy
cimport numpy as np

# if you want to use the Numpy-C-API from Cython
# (not strictly necessary for this example, but good practice)
np.import_array()

# cdefine the signature of our c function

cdef extern from "cross_correlation.h":
    void cross_correlation(double * X, double * Y, double * bins, int * C, 
                       int size_x, int size_y, int size_bins, int size_c) 

# create the wrapper code, with numpy type annotations
def cross_correlation_func(
        np.ndarray[double, ndim=1, mode="c"] X not None,
        np.ndarray[double, ndim=1, mode="c"] Y not None,
        np.ndarray[double, ndim=1, mode="c"] bins not None,
        np.ndarray[int, ndim=1, mode="c"] C not None):
    cross_correlation(
            <double*> np.PyArray_DATA(X),
            <double*> np.PyArray_DATA(Y),
            <double*> np.PyArray_DATA(bins),
            <int*> np.PyArray_DATA(C),
            X.shape[0],
            Y.shape[0],
            bins.shape[0],
            C.shape[0])
    return C 

from Rectangle cimport Rectangle

cdef class PyRectangle:
    cdef Rectangle c_rect

    def __cinit__(self, int x0, int y0, int x1, int y1):
        self.c_rect = Rectangle(x0, y0, x1, y1)

    def get_area(self):
        return self.c_rect.getArea()

    def get_size(self):
        cdef int width, height
        self.c_rect.getSize(&width, &height)
        return width, height

    def move(self, dx, dy):
        self.c_rect.move(dx, dy)

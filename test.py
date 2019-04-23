#module that talks to the C code
import numpy as np
import pylab
from cross_correlation import crosscor

x = np.arange(0, 1000, 10)
y = np.zeros(201)
z = crosscor(x, x+1, max_dt = 5)
print(z)

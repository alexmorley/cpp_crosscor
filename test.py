#module that talks to the C code
import numpy as np
import pylab
from cross_correlation import crosscor

x = np.arange(0, 1000, 10)
y = np.zeros(201)
z = crosscor(x, x+4, max_dt = 5)
print(z)
z = crosscor(x, x-5, max_dt = 5)
print(z)

def main():
    c = crosscor(x,y,max_dt=100,dt_step=1)
    c = crosscor(y,x,max_dt=100,dt_step=1)

import timeit
setup = """
from __main__ import main
import numpy as np
x = np.sort(np.random.rand(10000))*100
y = np.sort(np.random.rand(10000))*100+0.1
"""

print(timeit.timeit("main()", setup=setup,number=300))

#module that talks to the C code
import numpy as np
import pylab
import cross_correlation

def crosscor(X, Y, max_dt, dt_step=1):
    min_dt = -max_dt
    bins = np.array(np.arange(min_dt,max_dt,step=dt_step),dtype=np.float64)
    C = np.zeros(len(bins),dtype=np.int32)
    return cross_correlation.cross_correlation_func(np.array(X,dtype=np.float64), 
            np.array(Y,dtype=np.float64), bins, C)


x = np.arange(0, 1000, 10)
y = np.zeros(201)
z = crosscor(x, x+1, max_dt = 5)
print(z)

import numpy as np
a = np.array([1,2,3])
print "a\n", a 

b= np.array([[1,2],[3,4]])
print b

c = np.array([1,2,3,4], ndmin = 2)
print c

c = np.array([1,5,6,7], dtype = complex)
print c

d = c.reshape(2,2)
print d.ndim

f = np.arange(100)

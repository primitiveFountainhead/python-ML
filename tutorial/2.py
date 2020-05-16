import numpy as np

#Array creation

a = np.empty([3,2], dtype = float)
print a

b = np.zeros(5)
print b

c = np.ones([1,2], dtype=int)
print c

D = [4,6,3]
d = np.asarray(D)
print d

#from buffer
s = raw_input()

S = np.frombuffer(s, dtype='S1')
print S

#Range of Numbers

A = np.arange(5)
print A

B = np.arange(10,90, 3)
print B
#check out linespace and logspace

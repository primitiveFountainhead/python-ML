import numpy as np
#https://www.tutorialspoint.com/numpy/numpy_array_manipulation.htm
X = np.arange(0,50,5)
C = X.reshape(5,2)
print "Our Matrix\n", C

#tanspose
X_T = np.transpose(C)
print X_T

D = np.arange(10).reshape(5,2)
#print np.concatenate((C,D))

print C%D

#MAth and Stats
#https://www.tutorialspoint.com/numpy/numpy_statistical_functions.htm

#Copy and View
D = C
print id(D)
print id(C)
print"\n", D, "\n"
C = C +1
print id(D)
print id(C)

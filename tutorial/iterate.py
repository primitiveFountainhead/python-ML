import numpy as np

a = np.arange(0,60,5)
a = a.reshape(3,4)

print 'Original array is\n', a, '\n'
print 'Modified array is:'
for x in np.nditer(a):
    print x

for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print x

print 'First array is:' 
print a 
print '\n'  

print 'Second array is:' 
b = np.array([1, 2, 3, 4], dtype = int) 
print b  
print '\n' 

print 'Modified array is:' 
for x,y in np.nditer([a,b]):
    print "%d:%d" % (x,y)   
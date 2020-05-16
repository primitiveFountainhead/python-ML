import numpy as np

#SLICE EXAMPLE
a = np.arange(10)
print "a\n", a

s = slice(2,7,2)
print "s    ", s
print "a[s] "   ,a[s]

#numpy example

a = np.arange(10)
b = a[2:7:2]
print b

b = a[3:]
print b

b =np.array([[1,2,3],[4,5,6],[8,8,9],[4,5,6]])

#print b[1:4:2]

#item in second coloum
print "\n"
print b
#print b[..., 1]
#print b[..., 0:2]

#Advanced indexing
#integer Indexing

print b[[0,1,2],[2,0,1]]
print "\n"

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
   
print 'Our array is:' 
print x 
print '\n' 

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols] 
print y, "\n"  



#Boolean Array Indexing

print "Our Array is:\n", b
print "\n", b[b > 5]

#In this example, NaN (Not a Number) elements are omitted by using ~ (complement operator).
a = np.array([np.nan, 1,2,np.nan,3,4,5]) 
print a[~np.isnan(a)]

#Complex
a = np.array([1, 2+6j, 5, 3.5+5j]) 
print a[np.iscomplex(a)]
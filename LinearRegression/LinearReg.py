import csv
import numpy as np
from matplotlib import pyplot as plt 



class LinearRig:
    X = None
    Y = None
    itr = None
    n = None
    m = None
    sigma = None
    mu = None
    alpha = None
    theta = None


    def __init__(self, Xi, Yi, itri = 600, alpha = 0.01 ):
        self.X = np.copy(Xi)
        self.Y = np.copy(Yi)
        self.itr = itri
        self.m ,self.n = Xi.shape
        self.sigma = np.std(Xi, axis = 0)
        self.mu = np.mean(Xi,axis = 0)
       
        for i in range(self.n):
            self.X[:,i] = (self.X[:,i] - self.mu[i])/self.sigma[i]
      

      
        one = np.ones((self.m,1))
        self.X = np.concatenate((one,self.X), axis = 1)
        self.alpha = alpha
        self.theta = np.zeros((self.n + 1,1))
    
    def gradDsc(self):
        #J = []
        for i in range(self.itr):
            h = np.dot(self.X,self.theta)
            Dy = h - self.Y
            #J.append((np.dot(Dy.transpose(),Dy)/(2*self.m))[0,0])
            Dtheeta = (self.alpha * np.dot(self.X.transpose(),Dy))/self.m
            self.theta = self.theta - (Dtheeta)
        #print("Theta via gradient descent = ",self.theta, "\n")
      
   
           


    def normalEqu(self):
        xtransinv  = np.linalg.pinv(np.dot(np.transpose(self.X),self.X))
        X2invXtran = np.dot(xtransinv,self.X.transpose())
        self.theta = np.dot(X2invXtran, self.Y)
        #print("Theta via normal Equation = ", self.theta, "\n")

    def test(self,X):
        inp = np.copy(X)
        m = X.shape[0]
     
        for i in range(self.n):
            inp[:,i] = (X[:,i] - self.mu[i])/self.sigma[i]
        one = np.ones((m,1))
        inp = np.concatenate((one,inp), axis = 1)
     
        #print(np.dot(inp, self.theta))
        return np.dot(inp, self.theta)
       
        
        
     


        
       
    
    



def ReadCsv(fName):
    inData = []

    with open(fName,'r') as txt:
        inData =list(csv.reader(txt))

    data = np.array(inData).astype(np.float)
    n = len(data[0,:]) - 1
    m = len(data[:,0])
    X = data[:,0: -1 ]
    Y = np.array(data[:,-1]).reshape(m,1)
    return X , Y

X, Y = ReadCsv("ex1data1.txt")
test = np.array([[12.828],[18.945]])

L1 = LinearRig(X,Y)
L1.gradDsc()
L1.test(test)





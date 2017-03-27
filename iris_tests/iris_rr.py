import csv
import numpy as np
from numpy import linalg as LA
import pdb #pdb.set_trace(), debugger

# import csv
dataset = list(csv.reader(open('iris_train.csv','r')))

# convert string list to float
def myFloat(myList):
    return map(float, myList)

x = map(myFloat, dataset)

x = np.array(x)# X normalized as Numpy array, here, the good thing starts

xmean = np.mean(x, axis=0)

xc = np.subtract(x, xmean)#XC

xtc = xc.transpose()#Transpose of XC

c = np.dot(xtc, xc)

eig_val, eig_vec = LA.eig(c)

#Selects the best eigen vectors, 85%



pdb.set_trace()

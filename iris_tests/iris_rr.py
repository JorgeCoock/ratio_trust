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

c = np.dot(xtc, xc) #C MATRIX, this is the eig val and eig vec matrix

eig_val, eig_vec = LA.eig(c)

# ---- Heuristic that evaluates K best ratio rules k_positions are the RR---
# Covariance
cc = np.cov(c)

# Selects the best eigen vectors, 85%
sum_eigen_val = np.sum(eig_val)
eigthy = sum_eigen_val * 85 / 100 # 85% of eigenvectors sum

#Function that search for the max closest number from a list
takeClosest = lambda collection,num:max(collection,key=lambda x:(x-num))

k = [] #eigenvalues that sum 85% of  the eigenvectors
Z = []
print eigthy
while np.sum(k) < eigthy:
    Z = set(eig_val) - set(k)
    print Z
    rest = eigthy - np.sum(k)
    print rest
    k.append(takeClosest(Z,rest))
    print k

k_positions = []
for i in range(len(k)):
    k_positions.append(eig_vec[i])
# ---- Heuristic that evaluates K best ratio rules k_positions are the RR---



#pdb.set_trace()

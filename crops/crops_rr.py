import csv
import numpy as np
from numpy import linalg as LA
import pdb

with open('crops.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    log = list(reader)
    data, headers = log[:], log[:]
    headers = headers[0]
    data.pop(0)

dataset = []
for index, value in enumerate(data):
    dataset.append([value[0],value[2], value[7], value[9]])

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


def fill_holes_method(m,k,row):
    # Variables we need
    v = np.dot(m,k[0]) #V
    e_h = elimination_matrix(row)

    v_1 = np.dot(v,np.transpose(np.array(e_h)))
    b_1 = filter(lambda x: x != '?', row)

    x_concept = np.dot(inverse_values_array(v_1), b_1)

    d_val = np.dot(x_concept, v)

    pdb.set_trace()
    
    result = (np.dot(np.transpose(b_1), np.transpose(centered_version(e_h))) )


def missing_holes(row):
    total_count, positions = 0, []
    for index, record in enumerate(row):
        if record == '?':
            total_count += 1
            positions.append(index)
    return {'count': total_count, 'positions': positions}

def elimination_matrix(row):
    holes = missing_holes(row)
    if holes['count'] == 0:
        e_matrix = np.identity(len(row))
    else:
        e_matrix = np.identity(len(row)-holes['count'])
        e_matrix = e_matrix.tolist()
        for position_index, position in enumerate(holes['positions']):
            map(lambda x: x.insert(position, 0.0), e_matrix)
    return e_matrix

def inverse_values_array(arr):
    return map(lambda x: 1/x, arr)

def centered_version(arr):
    arr_mean = np.mean(arr, axis=0)
    return np.subtract(arr, xmean)

rrow = [1,'?',2,3]
e_matrix = elimination_matrix(rrow)

M = len(x[0])

fill_holes_method(M, k_positions, rrow)


### BUG
### K must be refered as k[0]

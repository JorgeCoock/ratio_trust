import numpy as np
from numpy import linalg as LA
import pdb

# return the array of ratio rules (using best k evaluation %85 eig val) of given matrix

def rr_generator(matrix):
    matrix = np.array(matrix)
    matrix_average = np.average(matrix, axis=0)

    print "Column averages: \n"+str(matrix_average)
    print ""

    x_c = np.subtract(matrix, matrix_average)

    x_c_transpose = x_c.transpose()

    c = np.dot(x_c_transpose, x_c)

    eigen_values, eigen_vectors = LA.eig(c)

    print "Initial Eigen values: \n"+str(eigen_values)
    print ""

    print "Initial Eigen vectors: \n"+str(eigen_vectors)
    print ""


    #FIXME: order descending the eigen values with correponding eigen vector changes
    # ---- Heuristic that evaluates K best ratio rules k_positions are the RR---
    sum_eigen_values = np.sum(eigen_values)

    eigthy_five_percent_of_values = sum_eigen_values * 85 / 100

    #Function that search for the max closest number from a list
    takeClosest = lambda collection,num:max(collection,key=lambda x:(x-num))

    k = [] #eigenvalues that sum 85% of  the eigenvectors
    Z = []
    while np.sum(k) < eigthy_five_percent_of_values:
        Z = set(eigen_values) - set(k)
        rest = eigthy_five_percent_of_values - np.sum(k)
        k.append(takeClosest(Z,rest))

    k_positions = []
    for i in range(len(k)):
        k_positions.append(eigen_vectors[i])
    # ---- Heuristic that evaluates K best ratio rules k_positions are the RR---

    print "Selected Eigen values: \n"+str(k)
    print ""
    print "Selected Eigen vectors (Ratio rules): \n"+str(k_positions)
    print ""

    return k, k_positions

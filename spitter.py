import pdb
import csv
import numpy as np
import math
import random

def split_set_tests(x):
    #calculates the 90% and the 10%
    ninety_x = int(math.ceil(len(x) * 0.9))
    ten_x = int(math.floor(len(x)* 0.1))
    #shuffle array
    y = np.random.permutation(x)
    #split x array into training and test
    training, test = y[:ninety_x,:], y[:ten_x,:]
    return training,test

def creates_holes(x):
    for value in x:
        #creates a random number smaller than the length
        ran = random.randint(1, len(value)-2)
        #creates a random sample from the size of the previous number
        y = random.sample(value, ran)
        #if can find the value it replaces it with - ?
        for index, item in enumerate(value):
            if item in y:
                value[index] = '?'
    return x

##test
## import csv
#dataset = list(csv.reader(open('iris_train.csv','r')))
#
## convert string list to float
#def myFloat(myList):
#    return map(float, myList)
#
#x = map(myFloat, dataset)
##x = np.array(x) does not accept strings
#x = np.array(x).astype('object')# X normalized as Numpy array, here

##test split_set_tests
#training, test = split_set_tests(x)

##test creates holes
#x = creates_holes(x)

random_rr = lambda k: random.sample(k, 1)
# Alternative
#def random_rr(k):
#    random_k = random.sample(k, 1)
#    return random_k
#
#test
#x = [1,2,3,4,5,6]
#y = random_rr(x)
#print y

#pdb.set_trace() #debugger

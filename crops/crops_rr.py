import csv
import numpy as np
import pdb
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rr_generator import rr_generator
from  spitter import split_set_tests, creates_holes
from fill_holes import filled_matrix
from accuracy_percentage import total_accuracy

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

matrix = map(myFloat, dataset)

training_set, test_set = split_set_tests(matrix)

eigen_values,ratio_rules = rr_generator(training_set)

test_set_with_holes = creates_holes(map(myFloat, test_set))

rebuilded_test_set = filled_matrix(test_set_with_holes, ratio_rules)

total_accuracy = total_accuracy(test_set, test_set_with_holes, rebuilded_test_set)

pdb.set_trace()

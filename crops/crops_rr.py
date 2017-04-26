import csv
import numpy as np
import pdb
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rr_generator import rr_generator

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

values,rules = rr_generator(matrix)

print values
print rules

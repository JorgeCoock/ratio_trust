import csv
import numpy as np
import pdb
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import init_main, myFloat

with open('crops.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    log = list(reader)
    data, headers = log[:], log[:]
    headers = headers[0]
    data.pop(0)

dataset = []
for index, value in enumerate(data):
    dataset.append([value[0],value[2], value[7], value[9]])

matrix = map(myFloat, dataset)

init_main(matrix)

# pdb.set_trace()
pdb.set_trace()

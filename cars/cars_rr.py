# Here we will use price[4], yearOfRegistration[7], kilometer[11], monthOfRegistration[12]

import pdb
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import csv

from main import init_main, myFloat

with open('/home/jorge/Documents/FIME/8/mineria/databases/autos.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    log = list(reader)
    data, headers = log[:], log[:]
    headers = headers[0]
    data.pop(0)

dataset = []
for index, value in enumerate(data):
    dataset.append([value[4],value[7], value[11], value[12]])

matrix = map(myFloat, dataset)

init_main(matrix)

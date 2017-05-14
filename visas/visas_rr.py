import pdb
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import csv

from main import init_main, myFloat

with open('/home/jorge/Documents/FIME/8/mineria/databases/shuffled/shuffle_visas.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    log = list(reader)
    data, headers = log[:], log[:]
    headers = headers[0]
    data.pop(0)

dataset = []

for index, value in enumerate(data):
    if value[6] == "NA":
        continue

    if value[1] == "DENIED":
        case_status = 0
    else:
        case_status = 1

    if value[5] == "N":
        full_time = 0
    else:
        full_time = 1

    dataset.append([case_status, full_time, value[6]])

matrix = map(myFloat, dataset)

init_main(matrix)

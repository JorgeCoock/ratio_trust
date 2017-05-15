# NFA es una lista que evalua porciones de tierra de un pais en base a su total de tierras en:
# crop_land,grazing_land,forest_land,fishing_ground,built_up_land,carbon,total,QScore dando un resultado final

import pdb
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import csv

from main import init_main, myFloat

with open('/home/jorge/Documents/FIME/8/mineria/databases/shuffled/shuffle_nfa.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    log = list(reader)
    data, headers = log[:], log[:]
    headers = headers[0]
    data.pop(0)

dataset = []
for index, value in enumerate(data):
    dataset.append([value[4], value[5], value[6],value[7], value[8], value[9], value[10], value[11]])

matrix = map(myFloat, dataset)

init_main(matrix)

import pdb
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import csv

from main import init_main, myFloat

COLUMN_RANGES_FILE_LOCATION = '/home/jorge/Documents/FIME/8/mineria/pia/youtube/'

with open('/home/jorge/Documents/FIME/8/mineria/databases/shuffled/shuffle_youtube.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    log = list(reader)
    data, headers = log[:], log[:]
    headers = headers[0]
    data.pop(0)

dataset = []
for index, value in enumerate(data):
    dataset.append(value)

matrix = map(myFloat, dataset)

init_main(matrix, COLUMN_RANGES_FILE_LOCATION)

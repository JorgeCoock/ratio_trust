#Census: geoid,name,state,county,tract,blockgroup,total,totalmoe,employed,employedmoe,unemployed,unemployedmoe,armedforces,armedforcesmoe,notinlaborforce,notinlaborforcemoe
import pdb
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import csv

from main import init_main, myFloat

COLUMN_RANGES_FILE_LOCATION = '/home/jorge/Documents/FIME/8/mineria/pia/census_jobs/'


with open('/home/jorge/Documents/FIME/8/mineria/databases/shuffled/shuffle_census_jobs.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    log = list(reader)
    data, headers = log[:], log[:]
    headers = headers[0]
    data.pop(0)

dataset = []
for index, value in enumerate(data):
    dataset.append([value[2],value[3],value[4],value[5], value[6], value[7],value[8], value[9], value[10], value[11], value[12], value[13],value[14],value[15]])

matrix = map(myFloat, dataset)

init_main(matrix, COLUMN_RANGES_FILE_LOCATION)

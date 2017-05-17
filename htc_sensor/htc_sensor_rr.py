# Gas sensors for home activity monitoring Data Set
#This dataset has recordings of a gas sensor array composed of 8 MOX gas sensors,
#and a temperature and humidity sensor. This sensor array was exposed to background
#home activity while subject to two different stimuli: wine and banana.
#The responses to banana and wine stimuli were recorded by placing the stimulus close to the sensors.
#The duration of each stimulation varied from 7min to 2h, with an average duration of 42min.
#This dataset contains a set of time series from three different conditions: wine,
#banana and background activity. There are 36 inductions with wine, 33 with banana and 31
#recordings of background activity. One possible application is to discriminate among background, wine and banana

#https://archive.ics.uci.edu/ml/datasets/Gas+sensors+for+home+activity+monitoring
import pdb
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import csv
import numpy as np

from main import init_main, myFloat

COLUMN_RANGES_FILE_LOCATION = '/home/jorge/Documents/FIME/8/mineria/pia/htc_sensor/'

with open('/home/jorge/Documents/FIME/8/mineria/databases/shuffled/shuffle_HT_Sensor_dataset.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    log = list(reader)
    data, headers = log[:], log[:]
    headers = headers[0]
    data.pop(0)

dataset = []
for index, value in enumerate(data):
    dataset.append([value[2],value[3], value[4], value[5], value[6],value[7],
        value[8],value[9],value[10],value[11]])

matrix = map(myFloat, dataset)

init_main(matrix, COLUMN_RANGES_FILE_LOCATION)

# pdb.set_trace()

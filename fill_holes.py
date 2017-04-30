import numpy as np
from random import randint
import pdb

def fill_hole(row, k_rules):
    row_filled = []
    for index, record in enumerate(row):
        if record == '?':
            rule = k_rules[randint(1,len(k_rules))-1]
            while True:
                random_rr_position = randint(1,len(rule))-1
                if index != random_rr_position and (row[random_rr_position] != '?'): break
            direct_relation = (abs(rule[random_rr_position]))/(abs(rule[index]))
            #result = row[random_rr_position]*direct_relation
            result = row[random_rr_position]/direct_relation
            row_filled.append(result)
        else:
            row_filled.append(record)
    return row_filled

def filled_matrix(set_with_holes, k_rules):
    filled_matrix = list(map((lambda row: fill_hole(row, k_rules)), set_with_holes))
    return filled_matrix

#k = [[9.99999802e-01,1.20653120e-04,5.93594013e-04,1.69677790e-04]] EXAMPLES
#row = ['?',6.65500000e+03,'?','?']

#a = fill_holes(k, row)
#print a

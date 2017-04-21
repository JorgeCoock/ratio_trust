import numpy as np
from random import randint

def fill_holes(k_rules, row):
    row_filled = []
    for index, record in enumerate(row):
        if record == '?':
            rule = randint(1,len(k_rules))-1
            while True:
                random_rr_position = randint(1,len(rule))-1
                if index != random_rr_position: break
            direct_relation = (abs(rule[random_rr_position]))/(abs(rule[index]))
            result = row[random_rr_position]/direct_relation
            row_filled.append(result)
        else:
            row_filled.append(record)
    return row_filled

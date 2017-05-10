import numpy as np
from random import randint
import pdb

def fill_hole(row, k_rules):
    """Receives a row with holes and returns a row without holes using Ratio Rules
    >>> fill_hole([204,214,254,'?'], [[-.53,-.58,-.60,-.0033],[-.56,-.27,.77,-.000228]])
    [204, 214, 254, 0.70395892162007978]
    >>> fill_hole([204,214,254,'?'],[[-.53,-.58,-.60,-.0033]])
    [204, 214, 254, 1.2949249620472782]
    """
    row_filled = []
    non_hole_positions, non_hole_values = non_holes_result(row)
    for index, record in enumerate(row):
        if record == '?':
            rr_predictions = []
            for non_h_index, non_hole_value in enumerate(non_hole_values):
                for k_index, k_val in enumerate(k_rules):
                    rr_predictions.append(non_hole_value/(abs(k_rules[k_index][non_hole_positions[non_h_index]])/abs(k_rules[k_index][index])))
            row_filled.append(np.mean(rr_predictions))
        else:
            row_filled.append(record)
    return row_filled


def filled_matrix(set_with_holes, k_rules):
    """
    >>> filled_matrix([[204,214,254,'?']], [[-.53,-.58,-.60,-.0033],[-.56,-.27,.77,-.000228]])
    [[204, 214, 254, 0.70395892162007978]]
    """
    filled_matrix = list(map((lambda row: fill_hole(row, k_rules)), set_with_holes))
    return filled_matrix

def non_holes_result(row):
    """Returns the positions and values of given row cells without '?s'
    >>> non_holes_result([1,2,'?',4])
    ([0, 1, 3], [1, 2, 4])
    """
    positions, values = [],[]
    for index, value in enumerate(row):
        if value != '?':
            positions.append(index)
            values.append(value)
    return positions, values

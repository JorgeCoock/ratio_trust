import numpy as np

def get_accuracy_percentage(original_row, predicted_row):
    a = np.array(original_row)
    b = np.array(predicted_row)
    error = np.mean(a != b)
    print error
    error_percentage = error * 10
    accuracy_percentage = 100 - error_percentage
    return accuracy_percentage

# EXAMPLES
# original_row = [0.8129356725834412, 6655.0, 1351.6863411946172, 4632.1839446400145]
# predicted_row = [0.8029466725834412, 6655.0, 1352.6863411946172, 4732.1839446400145]
# a = get_accuracy_percentage(original_row, predicted_row)
# print a

# SOURCE
# http://stackoverflow.com/questions/20402109/calculating-percentage-error-by-comparing-two-arrays
# https://en.wikipedia.org/wiki/Arithmetic_mean

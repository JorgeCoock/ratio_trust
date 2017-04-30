import numpy as np

def get_accuracy_percentage(original_row, row_to_predict, predicted_row):
    percentages = []
    for index,value in enumerate(original_row):
        if row_to_predict[index] == '?':
            error = abs(value - predicted_row[index])
            if value == 0 and predicted_row[index] != 0:
                error_percentage = 100
            if value == 0 and predicted_row[index] == 0:
                error_percentage = 0
            else:
                error_percentage = (error * 100) / abs(value)
            if error_percentage > 100:
                error_percentage = 100
            accuracy_percentage = 100 - error_percentage
            percentages.append(accuracy_percentage)
    percentage_average = sum(percentages) / len(percentages)
    return percentage_average

def total_accuracy(original_set, set_with_holes, rebuilded_set):
    total_accuracy = []
    for index, value in enumerate(original_set):
        total_accuracy.append(get_accuracy_percentage(original_set[index], set_with_holes[index], rebuilded_set[index]))
    return np.average(total_accuracy)

# EXAMPLES
# CHANGE VALUES OF ARRAY TO GET DIFFERENT ACCURACY
# original_row = [0.8029466725834412, 6655.0, 1352.6863411946172, 4732.1839446400145]
# row_to_predict = ['?',6.65500000e+03,'?','?']
# predicted_row = [0.8029466725834412, 6655.0, 1352.6863411946172, 4732.1839446400145]
# a = get_accuracy_percentage(original_row, row_to_predict, predicted_row)
# print a

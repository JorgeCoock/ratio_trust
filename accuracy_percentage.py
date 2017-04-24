def get_accuracy_percentage(original_row, row_to_predict, predicted_row):
    percentages = []
    for index,value in enumerate(original_row):
        if row_to_predict[index] == '?':
            error = abs(value - predicted_row[index])
            error_percentage = (error * 100) / value
            if error_percentage > 100:
                error_percentage = 100
            accuracy_percentage = 100 - error_percentage
            percentages.append(accuracy_percentage)
    percentage_average = sum(percentages) / len(percentages)
    return percentage_average


# EXAMPLES
# CHANGE VALUES OF ARRAY TO GET DIFFERENT ACCURACY
# original_row = [0.8029466725834412, 6655.0, 1352.6863411946172, 4732.1839446400145]
# row_to_predict = ['?',6.65500000e+03,'?','?']
# predicted_row = [0.8029466725834412, 6655.0, 1352.6863411946172, 4732.1839446400145]
# a = get_accuracy_percentage(original_row, row_to_predict, predicted_row)
# print a

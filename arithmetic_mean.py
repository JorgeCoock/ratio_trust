def get_accuracy_percentage(original_row, predicted_row):
    total_percentage = 0
    for index,value in enumerate(original_row):
        error = abs(value - predicted_row[index])
        error_percentage = (error * 100) / value
        if error_percentage > 100:
            error_percentage = 100
        accuracy_percentage = 100 - error_percentage
        total_percentage += accuracy_percentage
        # print "------"
        # print error_percentage
    percentage_average = total_percentage / len(original_row)
    return percentage_average


# EXAMPLES
# CHANGE VALUES OF ARRAY TO GET DIFFERENT ACCURACY
# original_row = [0.8029466725834412, 6655.0, 1352.6863411946172, 4732.1839446400145]
# predicted_row = [0.8029466725834412, 6655.0, 1352.6863411946172, 4732.1839446400145]
# a = get_accuracy_percentage(original_row, predicted_row)
# print a

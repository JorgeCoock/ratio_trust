from decimal import *
import csv
from csv import reader
import pdb

dataset = []
max_values = []
min_values = []
ranges = []
percentage = Decimal(0.33)
number_of_rows_in_ranges = []

# with open('test.csv', 'rU') as f:
#     reader = csv.reader(f)
#     next(reader)     # Skip header row
#     for row in reader:
#         dataset.append(row)

def init(dataset, file_location):
    total_records = len(dataset)
    number_of_columns = len(dataset[0])
    for x in range(number_of_columns):
        #max_of_column = max(Decimal(column[x].replace(',', '')) for column in dataset)
        #min_of_column = min(Decimal(column[x].replace(',', '')) for column in dataset)
        max_of_column = max(Decimal(column[x]) for column in dataset)
        min_of_column = min(Decimal(column[x]) for column in dataset)
        max_values.append(max_of_column)
        min_values.append(min_of_column)
        ranges.append([])
        number_of_rows_in_ranges.append([])

    for index in range(number_of_columns):
        difference = max_values[index] - min_values[index]
        step = difference * percentage
        change = min_values[index]
        while(change < max_values[index]):
            aux = change + step
            new_range = [change, aux]
            ranges[index].append([change, aux])
            change = aux

    for i,column in enumerate(ranges):
        for r in column:
            number_of_rows_in_ranges[i].append(0)

    for row in dataset:
        for index,value in enumerate(row):
            for ind,r in enumerate(ranges[index]):
                if Decimal(value) >= r[0] and Decimal(value) <= r[1]:
                    number_of_rows_in_ranges[index][ind] += 1
                    break

    text_file = open(file_location+"range_list.txt", "w")
    for index,column in enumerate(ranges):
        text_file.write("La columna %s\n" % index)
        text_file.write("------------------------\n")
        for i,r in enumerate(column):
            total = number_of_rows_in_ranges[index][i]
            percentage_of_row = (total*100)/float(total_records)
            text_file.write("Rangos entre: %.2f - %.2f || instancias: %s\n" % (r[0], r[1], total))
            text_file.write("Porcentaje es: "+str(percentage_of_row)+" \n")
            text_file.write("------------------------\n")
        text_file.write("\n\n")

    text_file.close()

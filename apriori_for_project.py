from decimal import *
import csv
from csv import reader
import itertools
import numpy as np
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# MODIFICAR DE ACUERDO A LO QUE OCUPEMOS
minimum_support_count = 10
minimum_conf = 0.60
#

dataset = []
max_values = []
min_values = []
ranges = []
unique_values = []
percentage = Decimal(0.10)
dataset_of_ranges = []
rules = []

# Leemos dataset
with open(input_file, 'rU') as f:
    reader = csv.reader(f)
    next(reader)     # Skip header row
    for row in reader:
        dataset.append(row)
        dataset_of_ranges.append([])

# Obtenemos el numero de columnas y su valor maximo y minimo de la misma para
# poder obtener los rangos.
number_of_columns = len(dataset[0])
for x in range(number_of_columns):
    max_of_column = max(Decimal(column[x].replace(',', '')) for column in dataset)
    min_of_column = min(Decimal(column[x].replace(',', '')) for column in dataset)
    max_values.append(max_of_column)
    min_values.append(min_of_column)
    ranges.append([])

# Aqui es donde obtenemos los rangos
for index in range(number_of_columns):
    difference = max_values[index] - min_values[index]
    step = difference * percentage
    change = min_values[index]
    while(change < max_values[index]):
        aux = change + step
        new_range = [change, aux]
        ranges[index].append([index, change, aux])
        change = aux

# Agrupacion de cada columna de cada row en su rango correspondiente.
for i,row in enumerate(dataset):
    for index,value in enumerate(row):
        dataset_of_ranges[i].append([])
        for ind,r in enumerate(ranges[index]):
            if Decimal(value) >= r[1] and Decimal(value) <= r[2]:
                dataset_of_ranges[i][index] = [index,ind]
                break

# Ahora obtenemos nuestros valores unicos
for row in dataset_of_ranges:
    for value in row:
        if value not in unique_values:
            unique_values.append(value)

# Primera iteracion
for value in unique_values:
    times_of_appearance = sum(x.count(value) for x in dataset_of_ranges)
    if times_of_appearance < minimum_support_count:
        unique_values.remove(value)

# Iteracion 2 en adelante, hasta que ya no tenga itemsets. Se eligen los itemsets de la iteracion pasada
# que aparezcan mas veces que el minimum_support_count
for i in range(number_of_columns):
    # Se obtienen las combinaciones posibles.
    combinations = list(itertools.combinations(unique_values, i))
    list_of_itemsets = []

    # Calcular cuantas veces aparece cada combinacion.
    for combination in combinations:
        times_of_appearance = 0
        for row in dataset_of_ranges:
            is_present = all(x in row for x in combination)
            if is_present:
                times_of_appearance += 1
        if times_of_appearance >= minimum_support_count:
            list_of_itemsets.append(combination)

    if not list_of_itemsets:
        list_of_itemsets = last_list_of_itemsets
        break
    else:
        last_list_of_itemsets = list_of_itemsets

# Ya que obtuvimos nuestro itemsets de valores que son mayor que el umbral aceptado.
# Obtenemos sus subsets y valores necesarios.
for itemset in list_of_itemsets:
    combinations = []
    times_of_appearance_of_itemset = 0
    for row in dataset_of_ranges:
        is_present = all(x in row for x in itemset)
        if is_present:
            times_of_appearance_of_itemset += 1
    for i in range((len(itemset))):
        if i != 0:
            combinations += list(itertools.combinations(itemset, i))
    for s in combinations:
        times_of_appearance = 0
        for row in dataset_of_ranges:
            is_present = all(x in row for x in s)
            if is_present:
                times_of_appearance += 1
        confidence = float(times_of_appearance_of_itemset) / float(times_of_appearance)
        if confidence >= minimum_conf:
            a = list(s)
            b = list(itemset)
            c = confidence
            for value in a:
                b.remove(value)
            times_of_y = 0
            for row in dataset_of_ranges:
                is_y_present = all(x in row for x in b)
                if is_y_present:
                    times_of_y += 1
            support = float(times_of_appearance_of_itemset) / float(len(dataset_of_ranges))
            push = (float(times_of_appearance_of_itemset) * float(len(dataset_of_ranges))) / (float(times_of_appearance) * float(times_of_y))
            rules.append([a,b,c,support, push])

text_file = open(output_file, "w")
for rule in rules:
    text_file.write("------------------------------------\n")
    for item in rule[0]:
        text_file.write("%s \n" % ranges[item[0]][item[1]])
    text_file.write("\nentonces \n")
    for item in rule[1]:
        text_file.write("%s \n" % ranges[item[0]][item[1]])
    text_file.write("\ncon \n")
    text_file.write("Confianza: %s%%\n" % (rule[2] * 100))
    text_file.write("Apoyo: %s\n" % rule[3])
    text_file.write("Empuje %s\n" % rule[4])
    text_file.write("\n--------------------------------\n\n")

text_file.close()

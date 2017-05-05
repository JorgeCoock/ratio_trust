import random
import sys

file_name = sys.argv[1]
f = open(file_name, "r")
li = f.readlines()
f.close()
# Remove next line if no headers
li.pop(0)
random.shuffle(li)

new_file_name = "shuffle_"+f.name

f = open(new_file_name, "w")
f.writelines(li)
f.close()

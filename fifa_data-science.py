import csv
# import numpy
path = "fifa18_clean.csv"

file = open(path)

reader = csv.reader(file)

header = next(reader)
data = [row for row in reader]
print(header)
print(data[0])
# lines = [line for line in open(path)]
# print(lines[0])
# for line in file:
# 	print(line)







# /home/sonabayim/project/datascience/venv/fifa/fifa18_clean.csv
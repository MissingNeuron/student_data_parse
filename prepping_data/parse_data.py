import csv

f = open('C:/Users/Max/Desktop/students_data/complete/complete.csv')
reader = csv.reader(f)

elem = []

for row in reader:
    elem.append(row)
import csv
with open('data/trees.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
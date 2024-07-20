import csv

with open('../data/transactions.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

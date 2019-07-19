import csv

tarif = []
with open('tarif.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        row_
        tarif.append(row)

print(tarif[0])
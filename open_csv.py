import csv

tarif = []
with open('tarif.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        att = row[0].split(',')
        tarif.append(att)

print(tarif[0])
print(tarif[7])

# kecamatan     : 1
# reg           : 3
# estimasi reg  : 4
# oke           : 5
# estimasi oke  : 6
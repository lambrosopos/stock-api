import csv

with open('prac.txt', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    content = [x for x in csv_reader]

    print(content)

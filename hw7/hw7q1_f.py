import csv

average_dict = {}
with open('hw7/averages.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        id = row[0]
        first = row[1]
        last = row[2]
        average = row[3]
        points = row[4]
        average_dict[id] = [first, last, average, points]


print(average_dict)
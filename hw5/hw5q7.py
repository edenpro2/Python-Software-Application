# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 5 Questions 7

import csv

# section a
cid = 0
amnt = 0
item = ""
cost = 0
total = 0


with open('hw5/items.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cid = row[0]
        amnt = row[3]
        item = row[1]
        cost = row[2]
        total = int(cost) * int(amnt)
        print("Customer #" + str(cid) + " purchased " + str(amnt) + " " + str(item) +
        "s for $" + str(cost) + " each, giving a total cost of $" + str(total)) 


# section b 
# ):
ids = [100, 200, 300, 400]
amount = 4
total = [0, 0, 0, 0]
with open('hw5/items.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        for id in ids:
            if id == int(row[0]):
                total[id % amount] += int(row[2]) * int(row[3])

for id in ids:
    print("Customer #" + str(id) + " had a total bill of $" + str(total[id % amount])) 
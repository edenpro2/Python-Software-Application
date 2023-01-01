# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 6 Question 4
import csv

def salary(hours, rate, isMarried, children):
    income = 0
    tax = 0.25
    if isMarried:
        tax = 0.20
    if children > 0:
        tax -= (children * 0.02)

    if hours > 60:
        income = 40 * rate 
        hours = hours - 40
        income += 20 * (1.5 * rate)
        hours = hours - 20
        income += hours * (2 * rate)
    elif hours > 40: # 40 < hours < 60
        income = 40 * rate 
        hours = hours - 40
        income += hours * (1.5 * rate)
    else:
        income = hours * rate 

    if tax < 0: # more than 10 kids
        return income

    return income * (1 - tax)


name = "" 
hours = 0
rate = 0
isMarried = False
numOfChildren = 0

with open('hw6/employees.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[0]
        hours = int(row[1])
        rate = int(row[2])
        isMarried = bool(row[3])
        numOfChildren = int(row[4])
        print(name + " worked " + str(hours) + 
        " hours at $" + str(rate) + 
        " and received a gross salary of $" + 
        str(salary(hours, rate, isMarried, numOfChildren)))

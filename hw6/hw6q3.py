# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 6 Question 3
import csv

def salary(hours, rate):
    income = 0
    if hours > 60:
        income = 40 * rate 
        hours = hours - 40
        income += 20 * (1.5 * rate)
        hours = hours - 20
        income += hours * (2 * rate)
        return income
    elif hours > 40: # 40 < hours < 60
        income = 40 * rate 
        hours = hours - 40
        income += hours * (1.5 * rate)
        return income
    else:
        income = hours * rate 
        return income


name = "" 
hours = 0
rate = 0

with open('hw6/employees.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[0]
        hours = int(row[1])
        rate = int(row[2])
        print(name + " worked " + str(hours) + 
        " hours at $" + str(rate) + 
        " and received a gross salary of $" + str(salary(hours, rate)))

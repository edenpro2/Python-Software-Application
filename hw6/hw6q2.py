# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 6 Question 2

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
        income = 40 * rate 
        hours = hours - 40
        return income

hours = 0
rate = 0
while True:
    hours = input("Enter hours: ")
    rate = input("Enter rate per hour: ")
    if hours == 'Done' or rate == 'Done':
        exit(0)
    print(str(salary(int(hours),int(rate))))
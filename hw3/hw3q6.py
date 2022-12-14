# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 3 Question 6


def moreThan(der : int, base : int):
    return int(der >= base)


def GetDiscount(spent):
    return moreThan(spent, 500) * spent * 0.90 +\
           moreThan(spent, 1000) * spent * 0.80 +\
           moreThan(spent, 2000) * spent * 0.75 +\
           (moreThan(spent, 3000) * (2000) * 0.70 + (spent - 2000) * 0.60)


spent = int(input("How much did customer spend: "))

print("Spent $" + str(spent) + " and discounted to " + str(GetDiscount(spent)))
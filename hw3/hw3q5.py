# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 3 Question 5


def getsMortgage(age : int, isMarried : bool, hasChildren : bool):
    return bool(hasChildren) or (age >= 30)  


age = int(input("Enter age: "))
isMarried = bool(int(input("Enter 0 - single, 1 - married: ")))
hasChildren = bool(int(input("Enter 0 - no children, 1 - has children: ")))
print("Entitled to cheap mortgage: " + str(getsMortgage(age, isMarried, hasChildren)))


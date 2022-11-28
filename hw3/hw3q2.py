# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 3 Question 2


class Student:
     def __init__(this, id: int, sex: int, army: bool, credits: int, height: float, weight: float):
        this.id = id
        this.sex = sex
        this.army = army
        this.credits = credits
        this.height = height
        this.weight = weight


def Acceptance(s : Student):
    return ((s.weight >= 60.0 and s.height >= 1.7 and s.sex == 0) | (s.weight >= 70.0 and s.height >= 1.8 and s.sex == 1)) and\
         s.credits >= 85 and s.army == True 

id = int(input("Enter id: "))
sex = int(input("Enter sex (0 - F, 1 - M): "))
army = bool(input("Enter 0 if no army service, 1 if you served: "))
credits = int(input("Enter number of credits completed: "))
height = float(input("Enter your height [ex: 1.54]: "))
weight = float(input("Enter your weight in kilos: "))

myStudent = Student(id, sex, army, credits, height, weight)

print("Student " + str(myStudent.id) + " is acceptable as a security person: " + str(Acceptance(myStudent)))
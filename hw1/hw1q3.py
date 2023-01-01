# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 1 Question 3

from enum import IntEnum

class Class:
    def __init__(self, name: str, grades: list, weight: int):
        self.name = name
        self.grades = grades
        self.weight = weight

class Points(IntEnum):
    math = 6
    physics = 6
    psychology = 5
    chemistry = 3
    history = 3


def GetGrades(grade_type):
    n = int(input("Enter number of " + grade_type + " grades : "))
    return list(map(int, input("Enter grades : ").strip().split()))[:n]


def WeightedAverage(classes: list[Class]):
    sum_of_grades = 0
    sum_of_weights = 0
    for c in classes:
        for g in c.grades:
            sum_of_grades += g * c.weight
            sum_of_weights += c.weight
    return sum_of_grades / sum_of_weights


student_name = input("Enter student name: ")

# science
math = Class("math", GetGrades("math"), int(Points.math))
physics = Class("physics", GetGrades("physics"), int(Points.physics))
chem = Class("chemistry", GetGrades("chemistry"), int(Points.chemistry))

science = []
science.append(math)
science.append(physics)
science.append(chem)

science_avg = WeightedAverage(science)

# social sciences 
psych = Class("psychology", GetGrades("psychology"), Points.psychology)
history = Class("history", GetGrades("history"), Points.history)

social = []
social.append(psych)
social.append(history)

social_avg = WeightedAverage(social)

# overall
total = []
total.extend(science)
total.extend(social)

total_avg = WeightedAverage(total)

print(student_name + " had a grade of " + str(round(science_avg, 2)) + " in his science courses and " 
    + str(round(social_avg, 2)) + " in his social science courses." + '\n' + 
    "His weighted average was " + str(round(total_avg, 2)))


exit(0)

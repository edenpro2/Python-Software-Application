# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 1 Question 2

from statistics import stdev


def GetGrades(grade_type):
    n = int(input("Enter number of " + grade_type + " grades : "))
    return list(map(int, input("Enter grades : ").strip().split()))[:n]


def Average(grades:list[int]):
    return sum(grades) / len(grades)    


student_name = input("Enter student name: ")

# science
math = GetGrades("math")
physics = GetGrades("physics")
chem = GetGrades("chemistry")

science = []
science.extend(math)
science.extend(physics)
science.extend(chem)

science_avg = Average(science)

# social sciences
psych = GetGrades("psychology")
history = GetGrades("history")

social = []
social.extend(psych)
social.extend(history)

social_avg = Average(social)

# overall
total = []
total.extend(science)
total.extend(social)

total_avg = Average(total)

print(student_name + " had a grade of " + str(round(science_avg, 2)) + " in his science courses and " 
    + str(round(social_avg, 2)) + " in his social science courses." + '\n' + 
    "His overall average was " + str(round(total_avg, 2)) + " with a standard deviation of " + str(round(stdev(total), 2)))


exit(0)

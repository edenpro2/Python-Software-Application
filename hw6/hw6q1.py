# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 6 Question 1


def gradeToLetter(grade):
    if 0 < grade < 60:
        return 'F'
    if grade < 70:
        return 'D'
    if grade < 80:
        return 'C'
    if grade < 90:
        return 'B'
    else:
        return 'A'


grade = ""
while True:
    grade = input("Enter grade ['Done' to exit]: ")
    if grade == 'Done':
        exit(0)
    print(gradeToLetter(int(grade)))
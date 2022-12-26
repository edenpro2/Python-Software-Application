# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 5 Questions 2


a = 0
b = 25
avg = 0
sum = 0

while a < b:
    a += 1
    if a % 2 != 0:  # if a is odd
        sum += a
        avg += (a/b)
        print("a=" + str(a) + " sum=" + str(sum))

    
print("Sum: " + str(sum) + '\n' +
        "Average: " + str(avg))
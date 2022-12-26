# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 5 Questions 3


b = 25
avg = 0
sum = 0

for i in range(26):
    sum += i
    avg += (i/b)
         
print("Sum: " + str(sum) + '\n' +
        "Average: " + str(avg))
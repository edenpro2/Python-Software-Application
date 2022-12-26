# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 5 Questions 5


current = 0
total_entered = 0
sum = 0
inp = ""

while inp != 'Done':
    inp = input("Enter 'Done' to stop or a number: ")
    try:
       current = int(inp)
       total_entered += 1
       sum += current
    except:
        if inp != 'Done':
            print("Not valid")
    

print("Total entered: " + str(total_entered) + '\n' + "Sum: " + str(sum) + '\n' + "Average: " + str(sum/total_entered))

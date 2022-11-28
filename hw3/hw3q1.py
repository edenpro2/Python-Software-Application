# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 3 Question 1

def IsEqual(a, b):
        return a == b


input1 = input("Enter first pair: ")
input2 = input("Enter second pair: ")
pair1 = tuple(map(int, input1.strip().split(' ')))
pair2 = tuple(map(int, input2.strip().split(' ')))

print("Are the 2 pairs identical?")
print(IsEqual(pair1,pair2))
print("First of each identical? " + str(IsEqual(pair1[0], pair2[0])))
print("Second of each identical? " + str(IsEqual(pair1[1], pair2[1])))
for x in pair1:
    for y in pair2:
        print(str(x) + " in first pair and " + str(y) + " in second pair"
        + " are identical? " + str(IsEqual(x,y)))
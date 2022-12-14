# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 3 Question 4


def IsEqual(a, b):
        return a == b


# Try block
try:
    input1 = input("Enter first pair: ")
    pair1 = tuple(map(int, input1.strip().split(' ')))
except:
    print("Not valid")
    exit(1)
try:
    input2 = input("Enter second pair: ")
    pair2 = tuple(map(int, input2.strip().split(' ')))
except:
    print("Not valid")
    exit(1)
# End of try block

print("Are the 2 pairs identical?")
print(IsEqual(pair1,pair2))
print("First of each identical? " + str(IsEqual(pair1[0], pair2[0])))
print("Second of each identical? " + str(IsEqual(pair1[1], pair2[1])))
for x in pair1:
    for y in pair2:
        print(str(x) + " in first pair and " + str(y) + " in second pair"
        + " are identical? " + str(IsEqual(x,y)))
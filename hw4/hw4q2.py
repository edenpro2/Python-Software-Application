# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 4 Question 2
import re

file = open("hw4/file.txt", "r")
lines = file.read()

# Print contents of file 
print("File.txt:\n" + str(lines))

splitlines = lines.split('\n')

string = splitlines[0].split(',')
sentences = splitlines[1:]

newlist = []
for i in range(0,3):
    newlist.append(string[i] + " " + sentences[i])

print(newlist)
longstr = ""

for i in range(0, len(newlist)):
    longstr += newlist[i] + " "

longstr = longstr.lower()
print(longstr)

words = longstr.split(' ')
words.sort()

print(words)



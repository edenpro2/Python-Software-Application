# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 5 Questions 6


print("Hello there!", end = '') 


inp = ""
allfruits = ""

while inp != 'Done':
    inp = input("Enter 'Done' to stop or enter a fruit: ")
    if (inp != 'Done'):
        allfruits += " " + ' '.join(inp)
        
print(allfruits)
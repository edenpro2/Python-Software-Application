# Eden Amiga
# Python Software Applications - Fall 2022
# Homework 4 Question 1

 
# Section a
students = ["Chana", "Rachel", "Leah", "Julie", "Simone", "Danielle", "Ruth", "Lorry", "Janet"]
print(str(students))

# Section b
students.append("Tzippy")
print(str(students))

# Section c
students.remove("Rachel")
print(students)

# Section d
students.extend(["Nehama", "Sarit", "Michal", "Naomi"])
print(students)

# Section e
students.remove("Chana")
students.remove("Julie")
students.remove("Simone")
print(students)

# Section f
students.sort()
print(students)

# Section g
selection = students[:3]
print(selection)

# Section h
selection = students[-3:]
print(selection)
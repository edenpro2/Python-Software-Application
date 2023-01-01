id_grades = {
    134 : ['John Cohen', 85.4, 65],
    253 : ['Sara Berger', 73.9, 47],
    456 : ['Chana Levi', 94.6, 88],
    654 : ['Yochai Fried', 88.9, 102]
}
v = int(input("Enter id: "))
pers = id_grades[v]
print(pers[0] + " ID Number " + str(v) + " has accumalted " +
 str(pers[2]) + " points with an average of " + str(pers[1]))
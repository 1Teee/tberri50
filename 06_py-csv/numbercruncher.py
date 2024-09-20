# The Duo-lingos -- Tawab Berri, Jacob Lukose, Jack Blair
# SoftDev
# K06 - Review on .csv's and accessing files, as well as the random library and dictionaries in Python.
# 2024-09-18 - 19
# time spent: 0:50

'''
DISCO:
...
QCC:
...
HOW THIS SCRIPT WORKS:
This script first splits up the data into both a 2d list and a dictionary. This is because a
2d list is easier to work with because of its accessibility in terms of index and ability to store
different types of data. The 2d list stores lists of length 2, which contain the occupation string, 
and a percentage value which adds the percentage for the aforementioned occupation onto the 
percentage in the previous list, to make the whole random selection probability system easier. 
The script then creates a random integer representing a percentage values, and selects the 
corresponding percentage value, then prints its respective occupation stored as a string.
'''

import random
f = open("occupations.csv", "r")
text = f.read()
# convert data from .csv to a string, which we will then manipulate and transform into a dictionary

#print(text)

dict = {}
rows = 22
prob = [[0, ""]] * rows
#print(prob)

jobs = text.split('\n')
jobs = jobs[1:-1] #first line in a csv is always the column identifiers/labels, last line is "total"

i = 0 
while i < len(jobs) - 1:
    if jobs[i][0] != "\"":
        job = jobs[i].split(",")
        dict[job[0]] = float(job[1])
        prob[i] = [job[0], float(job[1])]
    else:
        job = jobs[i].split("\"")
        dict[job[1]] = float(job[2][1:])
        prob[i] = [job[1], float(job[2][1:])]
    if (i > 0):
        prob[i][1] = prob[i-1][1] + prob[i][1]
    i += 1
    
print(dict)
#print(prob)

r = random.randint(0, 99)
#print(r)
ret = ""
for job in prob:
    if job[1] > r:
        ret = job[0]
        break
print(ret)
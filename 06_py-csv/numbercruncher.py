# The Duo-lingos -- Tawab Berri, Jacob Lukose, Jack Blair
# SoftDev
# K06 - Review on .csv's and accessing files, as well as the random library and dictionaries in Python.
# 2024-09-18
# time spent: 0:30

'''
DISCO:
...
QCC:
...
HOW THIS SCRIPT WORKS:

'''

import random
f = open("occupations.csv", "r")
text = f.read()
# convert data from .csv to a string, which we will then manipulate and transform into a dictionary

print(text)

dict = {}
#pdict = {} # dictionary specific for percentage calculations
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
        if (i >= 1):
            print(prob[i][1])
            prob[i][1] = prob[i-1][1] + prob[i][1]
    i += 1
    print(i)
    
print(dict)
print(prob)




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
pdict = {} # dictionary specific for percentage calculations
jobs = text.split('\n')
jobs = jobs[1:-1] #first line in a csv is always the column identifiers/labels, last line is "total"
#totalpercentage = 0   Used for debugging purposes

i = 0 
while i < len(jobs) - 1:
    if jobs[i][0] != "\"":
        job = jobs[i].split(",")
        dict[job[0]] = job[1]
        #totalpercentage += float(job[1])
    else:
        job = jobs[i].split("\"")
        dict[job[1]] = job[2][1:]
        #totalpercentage += float(job[2][1:])
    i += 1

print(dict)
#print(len(dict))
#print(totalpercentage)     Used for debugging purposes

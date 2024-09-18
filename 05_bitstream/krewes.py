import random
f = open("krewes.txt", "r")
text = f.read()

devos = text.split("@@@")

dict = {}
i = 0
while i < len(devos):
    dict[i] = devos[i]
    i+=1
    
print(dict)
n = random.randint(0, len(dict) -1)
print(n)

devoinfo = dict[n].split("$$$")
print("Period: " + devoinfo[0] + ", Name: " + devoinfo[1] + ", Ducky: " + devoinfo[2])
#Victor Casado
#VICTOOOOOORIOUS
#SoftDev
#K13 -- Putting occupations on a website with html
#2024-10-1
#time spent: 2.1 hours

import random as r


def pickrand():
    f = open("data/occupations.csv", "r")
    string = f.read()

    list = string.split("\n")
    list = list[1:len(list)-2] #removes example row, total row, and new line row

    names = []
    nums = []
#counter = 0
    for i in range(len(list)):
        if(list[i][0] == "\""):
            indexcomma = list[i][1:].index("\"") + 2
            indexat = list[i][1:].index("@")
            name = list[i][1:indexcomma - 1] #starts at first quote, ends at second quote
            num = list[i][indexcomma + 1:indexat]
            #print(list[i])
            #print(list[i][indexat])
        else:
            split = list[i].split("@")
            name = split[0].split(",")[0]
            num = split[0].split(",")[1]
        names.append(name)
        nums.append(float(num))
    #counter += 1
    #print(str(counter) + ": " + name)
#print(names)
#print(nums)
#print(dict)
    return r.choices(names, nums)[0]

def gettable():
    f = open("data/occupations.csv", "r")
    string = f.read()

    list = string.split("\n")
    list = list[1:len(list)-2] #removes example row, total row, and new line row

    dict = {}
    #counter = 0
    for i in range(len(list)):
        if(list[i][0] == "\""):
            indexcomma = list[i][1:].index("\"") + 2
            indexat = list[i][1:].index("@")
            name = list[i][1:indexcomma - 1] #starts at first quote, ends at second quote
            num = list[i][indexcomma + 1:indexat+1]
            link = list[i][indexat + 1:]
        else:
            split = list[i].split("@")
            name = split[0].split(",")[0]
            num = split[0].split(",")[1]
            link = split[1]
        dict.update({i:[name,num,link]})
        #counter += 1
        #print(str(counter) + ": " + name)
    #print(names)
    #print(nums)
    #print(dict)
    return dict

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"



@app.route("/wdywtbwygp")
def test_tmplt():

    return render_template( 'tablified.html', title="An Appropriate Title", roster = "Victor Casado, Tawab Berri, Jacob Lukose", TNPG = "VICTOOOOOORIOUS", heading = "A website that chooses a job for you and provides job info", job = pickrand(), dictionary = gettable())


if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)

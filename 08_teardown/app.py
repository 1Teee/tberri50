# The Duo-lingos -- Tawab Berri, Jacob Lukose, Jack Blair
# SoftDev
# K08 - Learnination Via Deconstruction
# 2024-09-20
# time spent: .2
'''
DISCO:
<note any discoveries you made here... no matter how small!>
When I try to install flask and run the code, i'm met with a warning.

QCC:
0. Java - When initializing an object that has arguments in its constructor
1. path files, or web links which are paths of their own type.
2. I do not know.
3. It will print "name", although I'm not sure what name actually is.
4. I don't think it will appear anywhere because it is returned by the function, not printed,
   no other print statements are in this code, so the value returned by the dunction cannot be
   printed anywhere else.
5. Java - When executing a pmethod without parameters that belongs to a different class.
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?




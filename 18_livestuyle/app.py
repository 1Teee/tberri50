'''
Tawab Berri
The Duo-lingos - Tawab Berri, Jacob Lukose, Jack Blair
SoftDev
2024-10-16
K18 - Serving html content with flask
time spent: 0 hrs
'''

# cited and adapted from victor casado's code

from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods = ['GET', 'POST'])
def foo():
    hone = "h1 foo"
    hthree = "nav foo"
    ttteee = "dis"
    ttwo = "dat"
    tone = "de udda ting"
    htwo = "main foo heading"
    pee = "The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start."
    foot = "Copyright Tawab Berri"
    return render_template("index.html", h1 = hone, h3 = hthree, ttt = ttteee, tt = ttwo, t = tone, h2 = htwo, p = pee, footer = foot)

if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run()
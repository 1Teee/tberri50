'''
Tawab Berri
The Duo-lingos - Tawab Berri, Jacob Lukose, Jack Blair
SoftDev
2024-10-08
K16 - Analyzing the different forms of server responses of user inputs.
time spent: 2.9 hrs
'''

# cited and adapted from victor casado's code

from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods = ['GET', 'POST'])
def login():
    print('!!!')
    if 'username' in session:
        print('!!')
        return redirect('/auth')
    else:
        return render_template("login.html")
    
@app.route('/auth', methods = ['GET', 'POST'])
def auth_login():
    if 'username' in session:
        return render_template("response.html", user = session['username'])
    if (request.method == 'POST'): login = request.form
    else: login = request.args
    print(login)
    username = login['username']
    password = login['password']
    session['username'] = username
    return render_template("response.html", user = username)

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    del session['username']
    return redirect('/')

if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run()
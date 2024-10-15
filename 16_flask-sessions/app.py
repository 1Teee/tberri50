'''
Tawab Berri
The Duo-lingos - Tawab Berri, Jacob Lukose, Jack Blair
SoftDev
2024-10-08
K15 - Analyzing the different forms of server responses of user inputs.
time spent: 2.9 hrs
'''

from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

logins = {"tawab" : "berri"}

@app.route('/')
def login():
    if 'username' in session:
        return redirect('/auth')
    else:
        return render_template("login.html")
    
@app.route('/auth')
def auth_login():
    if 'username' in session:
        return render_template("home.html", user = session['username'])
    login = request.args
    username = login['username']
    password = login['password']
    if username in logins:
        if logins[username] == password:
            session['username'] = username
            return render_template("home.html", user = username)
        else:
            return redirect('/')
    else:
        return redirect('/')
    
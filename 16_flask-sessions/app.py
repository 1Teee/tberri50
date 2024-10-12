'''
Tawab Berri
The Duo-lingos - Tawab Berri, Jacob Lukose, Jack Blair
SoftDev
2024-10-08
K15 - Analyzing the different forms of server responses of user inputs.
time spent: 2.4 hrs
'''
# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session as S

import testmod0
import secrets
import os

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = secrets.token_hex()#"blah blah blah" #os.urandom(32)


@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    #print("one\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)
    #print("***DIAG: request.args['username']  ***") this pair doesnt work because the variable "username" probably hasnt been defined yet.
    #print(request.args['username'])
    #print("***DIAG: request.headers ***")
    #print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    #print("\ntwo\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    #print("***DIAG: request.headers ***")
    #print(request.headers)
    if request.method == 'POST':
        u = request.form['username']
    elif (request.method == 'GET'): u = request.args['username']
    
    
    S['password'] = request.cookies.get('password')
    S['KEY'] = app.secret_key
    return render_template( 'response.html', user = u, form = request.method)  #response to a form submission

@app.route("/logout", methods=['GET', 'POST'])
def goodbye():
    S.pop('password')
    S.pop('KEY')
    return render_template( 'logout.html')


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

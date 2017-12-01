from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup(): 

    username = request.form['username']
    username_error = ""
    password = request.form['password']
    password_error = ""
    verify_password = request.form["verify_password"]
    verify_error = ""
    email= request.form["email"]
    email_error = ""


    if username =="":
        username_error= "Please enter something"
        username = ""
    elif len(username) <= 3 or len(username) >20 or " " in username:
        username_error = "Must have atleast 4 or more characters and no spaces"
        username = ""

    if password =="":
        password_error = "Please enter something"
        password=""
    elif len(password) <=3 or len(password)>20 or " " in password:
        password_error = "Must have between 4 and 20 characters and no spaces"
        password = ""
    if not (verify_password) == password:
        verify_error = "Passwords do not match"

    if len(email) <= 3 or len(email) > 20 or " " in email:
        email_error = "Please enter a valid email"    
    elif "@" and "."not in email:
        email_error = "Please enter a valid email"
        email =""
    elif "@" and "." in email:
        email = ""
        

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    
    else:
        return render_template('signup.html', username=username, 
            username_error= username_error,
            password= password,
            password_error=password_error,
            verify_password=verify_password,
            verify_error=verify_error,
            email = email,
            email_error = email_error
            )




app.run()

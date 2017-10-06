from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    
    return render_template("homepage.html")

@app.route("/confirmation", methods=["POST"])
def confirm():
    user_error =''
    password=request.form['password']
    confpassword=request.form['confpassword']
    email=request.form['email']
    username=request.form['username']
    password_error =''
    verify_error = ''
    email_error = ''
    email_list = list(email)
    if len(username) < 1:
        user_error = "Please enter a user name"
    elif len (username) <3 or len(username) >20:
        user_error = "Please enter a username between 3 and 20 characters"

    if len(password) <1:
        password_error = "Please enter a password"
    elif password != confpassword:
        password_error = "Passwords do not match"

    if len(confpassword)<1:
        verify_error = "Please verify the password"
    if len(email) > 0 and len(email)<3 or len(email)>20:
        email_error = "Please enter an email between 3 and 20 characters"
    elif email_list.count("@") != 1 or email_list.count(".") != 1:
        email_error = "Please enter a valid email example@domain.com"
    elif " " in list(email):
        email_error = "Please enter a valid email example@domain.com"


    if not user_error and not password_error and not verify_error and not email_error:
        return render_template("confirmation.html", username=username,)
    else:
        return render_template("homepage.html", username=username, user_error=user_error, email=email,password_error=password_error, verify_error=verify_error, email_error=email_error)

app.run()
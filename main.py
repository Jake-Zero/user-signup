from flask import Flask, request, render_template
import jinja2

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("signup.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    email = request.form["email"]
    username_error = ""
    password1_error = ""
    password2_error = ""
    email_error = ""
    if len(username) < 3 or len(username) > 20:
        username_error = "Username must be 3-20 characters long"
        username = ""
    else:
        if username.find(" ") >= 1:
            username_error = "Username must not include spaces"
            username = ""
    if len(password1) < 3 or len(password1) > 20:
        password1_error = "Password must be 3-20 characters long"
    else:
        if password1.find(" ") >= 1:
            password1_error = "Password must not include spaces"
    if password2 != password1:
        password2_error = "Passwords must match"
    if email != "":
        if len(email) < 3 or len(email) > 20:
            email_error = "Email must be 3-20 characters long"
            email = ""
        else:
            if email.find(" ") >= 1:
                email_error = "Email must not include spaces"
                email = ""
            elif email.find(".") == 0 and email.find("@") == 0:
                email_error = "Email must include at least 1 @ and ."
                email = ""
            elif email.find(".") == 0:
                email_error = "Email must include at least 1 ."
                email = ""
            elif email.find("@") == 0:
                email_error = "Email must include at least 1 @"
                email = ""
    if not username_error and not password1_error and not password2_error and not email_error:
        return render_template("login.html", username=username)
    else:
        return render_template("signup.html", username_error=username_error,password1_error=password1_error,password2_error=password2_error,email_error=email_error,username=username,email=email)
app.run()
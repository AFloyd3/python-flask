
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return '<h1> Welcome Home</h1>' 



@app.route("/greet")
def greet():
    myname = "Amber"
    return render_template("greet.html", name= myname)


@app.route("/evens")
def evens():
    return render_template("evens.html")

@app.route("/list")
def showlist():
    return render_template("list10.html")


@app.route("/google")
def google():
    return redirect("https://www.google.com")

@app.route("/error")
def error():
    return '<h1 style="color:red"> Error </h1>'

@app.route("/admin")
def admin():
    return redirect(url_for("error"))



if __name__== "__main__":
    app.run(host="0.0.0.0", port = 3000, debug=False)
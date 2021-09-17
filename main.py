from flask import Flask, redirect, url_for, render_template, request, flash, session
import mysql.connector
from settings import *

mycursor = db.cursor()

app = Flask(__name__)
app.secret_key = "hello"

#----------website----------
@app.route("/login", methods=["POST", "GET"])
def login():
    if "passwd" in session:
        return redirect(url_for("dashboard"))
    else:
        if request.method == "POST":
            userPasswd = request.form["passwd"]
            if userPasswd != "":
                if userPasswd == passwd:
                    session["passwd"] = userPasswd
                    return redirect(url_for("dashboard"))
                else:
                    flash(f"bitte gib das richtige Passwort ein", "info")
                    return redirect(url_for("login"))
            else:
                flash(f"bitte gib ein Passwort ein", "info")
                return redirect(url_for("login"))
        else:
            return render_template("index.html")

@app.route("/logout")
def logout():
    session.pop("passwd", None)
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if "passwd" in session:
        return render_template("dashboard.html")
    else:
        return redirect(url_for("login"))

@app.route("/input", methods=["POST", "GET"])
def userInput():
    if "passwd" in session:
        if request.method == "POST":
            walked = request.form["distance"]
            clan = request.form["clan"]
            if walked != "":
                print(walked)
                print(clan)
                mycursor.execute("UPDATE tbl_distance SET walked = walked + %s WHERE clan = %s", (walked, clan,))
                db.commit()
                return redirect(url_for("dashboard"))
            else:
                flash("bitte fülle alle felder aus")
                return redirect(url_for("userInput"))
        else:
            return render_template("input.html", clanList = clanList)
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

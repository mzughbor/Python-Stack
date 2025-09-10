from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "112b9bdd55ab9fd4d12e236c78afcb9a393ec16f71bbf5dc987d84729823bcbb"

@app.route('/')
def index():
    if 'number' not in session:
        session["number"] = random.randint(1, 100)
        session["status"] = None
        session["attempts"] = 0
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    user_guess = int(request.form["guess"])
    session["attempts"] += 1
    if session["attempts"] >= 5 and user_guess != session["number"]:
        session["status"] = "exceed"
    elif user_guess < session["number"]:
        session["status"] = "low"    
    elif user_guess > session["number"]:
        session["status"] = "high"
    else:
        session["status"] = "correct"
    
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

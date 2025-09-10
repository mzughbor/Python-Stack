from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey123'  # ✅ Add this line

""" 
@app.route('/user/<name>/<lname>')
def user(name, lname):
    return "Success!, Welcome " + name + " " + lname
"""

@app.route('/')
def home():
    return render_template("home.html", active="home")

@app.route('/about')
def about():
    return render_template("about.html", active="about")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        if not name or not message:
            flash("Please fill in all fields.", "error")
        else:
            flash(f"Thanks for your message, {name}!", "success")
            return redirect(url_for("contact"))
    return render_template("contact.html", active="contact")

if __name__ == "__main__":
    app.run(debug=True)
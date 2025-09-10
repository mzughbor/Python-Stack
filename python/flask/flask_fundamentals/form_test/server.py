from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def createUser():
    print("Got post info ------\n")
    print(request.form)
    nameFromForm = request.form['name']
    emailFromForm = request.form['email']
    
    #return render_template("show.html", nameOnTemp = nameFromForm, emailOnTemp = emailFromForm, data = request.form)
    
    return redirect("/show")

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)

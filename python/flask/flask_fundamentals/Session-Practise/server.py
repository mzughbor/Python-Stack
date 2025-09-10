from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "252b9bdd55ab9fd4d12e236c78afcb9a393ec16f71bbf5dc987d84729823bcbb"

@app.route('/')
def index():
    # home page with signup form
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post nfo")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "909b9bdd55ab9fd4d12e236c78afcb9a393ec16f71bbf5dc987d33729823bcbb"

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.jinja', counter=session['counter'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

# NINJA BONUS:+2
@app.route('/add_two')
def add_two():
    session['counter'] = session.get('counter', 0) + 1
    return redirect('/')

# NINJA BONUS
@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

# SENSEI BONUS
@app.route('/increment', methods=['POST'])
def increment():
    num = int(request.form['howMany'])
    session['counter'] = session.get('counter', 0) + num -1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

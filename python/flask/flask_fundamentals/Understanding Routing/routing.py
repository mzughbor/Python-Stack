from flask import Flask

myApp = Flask(__name__)
@myApp.route('/')
def hello_world():
    return "Hello World!"

@myApp.route('/champion')
def champion():
    return "Champion!"

@myApp.route('/say/<name>')
def welcome_people(name):
    return "Hi " + name + "!"

@myApp.route('/repeat/<int:num>/<smth>')
def repeate_me(num, smth):
    num = int(num)
    output = ""
    for i in range(num):
        output += smth + "<br>"
    return output

@myApp.errorhandler(404)
def pageNotFound(error):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    myApp.run(debug=True)
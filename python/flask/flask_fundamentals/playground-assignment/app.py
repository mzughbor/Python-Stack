from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/play/<int:itteration_num>')
def play_with_itter(itteration_num):
    return render_template("play.html", itteration_num=itteration_num)

@app.route('/play/<int:itteration_num>/<color>')
def user_with_color(itteration_num, color):
    return render_template("play.html", itteration_num=itteration_num, color_used=color)

if __name__ == "__main__":
    app.run(debug=True)

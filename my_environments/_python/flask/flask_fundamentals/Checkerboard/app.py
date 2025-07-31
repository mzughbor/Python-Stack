from flask import Flask, render_template

app = Flask(__name__)

# 25% 25% >>> 8 * 8  default, black and white
@app.route('/')
def home():
    return render_template("board.jinja", x_size= 25, y_size= 25)
    
# x rows, 8 default columns
@app.route('/<int:x>')
def one_param(x):
    return render_template("board.jinja", x_size= 25, y_size= 100/(x/2))

# x rows and y columns
@app.route('/<int:x>/<int:y>')
def two_params(x, y):
    return render_template("board.jinja", x_size= 100/(y/2), y_size= 100/(x/2))

# x rows, y cols, and two custom hex colors
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def full_params(x, y, color1, color2):
    #return render_template("board.jinja", x_size= 100/(y/2), y_size= 100/(x/2), color1=f'#{color1}', color2=f'#{color2}')
    # not hex / normal typing red black etc ...
    return render_template("board.jinja", x_size= 100/(y/2), y_size= 100/(x/2), color1=f'{color1}', color2=f'{color2}')

if __name__ == "__main__":
    app.run(debug=True)


# idea key >> https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/conic-gradient#checkerboard , mzughbor :)
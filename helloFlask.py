from flask import Flask , render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World</h1>'


@app.route('/render')
def index():
    return render_template('render.html')


if __name__ == '__main__':
    app.run(debug=True)
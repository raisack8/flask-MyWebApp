from ensurepip import bootstrap
from flask import Flask , render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/practice/top')
def p_top():
    return render_template('practice/top.html')

if __name__ == '__main__':
    app.run(debug=True)
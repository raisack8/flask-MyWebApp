from flask import Flask , render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

#----- Flask Practice -----

@app.route('/practice/top',methods=['GET','POST'])
def p_top():
    return render_template('practice/top.html')

@app.route('/practice/pre_color',methods=['GET','POST'])
def pre_color():
    return render_template('practice/pre_color.html')

@app.route('/practice/pre_food',methods=['GET','POST'])
def pre_food():
    return render_template('practice/pre_food.html')

@app.route('/practice/pre_season',methods=['GET','POST'])
def pre_season():
    return render_template('practice/pre_season.html')

@app.route('/practice/pre_result',methods=['GET','POST'])
def pre_result():
    return render_template('practice/pre_result.html')

if __name__ == '__main__':
    app.run(debug=True)
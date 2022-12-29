import datetime

from flask_sqlalchemy import SQLAlchemy

from flask import Flask , render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin,login_user,logout_user, login_required
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
import pytz
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = os.urandom(24)
# db = SQLAlchemy(app)
bootstrap=Bootstrap(app)

login_manager=LoginManager()
login_manager.init_app(app)

# SQLアルケミーがなかなか読み込まれない為断念
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at=db.Column(db.DateTime,nullable=False,
                       default =datetime.now(pytz.timezone('Asia/Tokyo')))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(20))

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
#region Flask tutorial
#endregion

if __name__ == '__main__':
    app.run(debug=True)
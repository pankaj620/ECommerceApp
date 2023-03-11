from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'market.db')
app.config['SECRET_KEY']='4d01a1f29a4da1f372eed5b5'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + os.path.join(basedir, 'market.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\filepath\\database\\market.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from Market import routes



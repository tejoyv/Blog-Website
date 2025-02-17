from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager 

app=Flask(__name__)
app.config['SECRET_KEY'] = '623f0bd79ad159786eb3bcb90244c38c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'     # for login route (restriction)

from Flask_Learn import routes  # declared here to avoid circular imports
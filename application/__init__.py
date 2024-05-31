from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/alx"
app.secret_key = 'me_dude'
client = PyMongo(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from application import views

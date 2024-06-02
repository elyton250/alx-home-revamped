
"""this module contains the routes for the flask app"""
from application import app, client, login_manager
from application.models import User
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

db = client.db # datababse initialisation



@login_manager.user_loader
def load_user(username):
    user = db.users.find_one({"username": username})
    if not user:
        return None
    return User(user['email'], user['username'])

# @app.route('/')
# @login_required
# def test():
#     return render_template('index-dash.html')
    


#login page implmentation
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db.users.find_one({"username": request.form.get('username')})
        if user and check_password_hash(user['password'], request.form.get('password')):
            user_obj = User(user['email'], user['username'])
            login_user(user_obj)
            print('I am reaching here')
            return redirect(url_for('index'))
        else:
            flash('Wrong user name or password')
    return render_template('login.html')


# # logout implementation
# @app.route('/logout')
# # @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))


#registering implementation
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Handle the signup
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')

#         # Create a new user
#         user = User(email, username)
#         user.password = generate_password_hash(password)

#         # Print the user data to be inserted
#         print(user.__dict__)

#         # Try to insert the user data into the database
#         try:
#             db.users.insert_one(user.__dict__)
#             flash('Account created successfully!')
#             return redirect(url_for('login'))
#         except Exception as e:
#             print("An error occurred while inserting the user data: ", e)

#     return render_template('register.html')


# @app.route('/register', methods=['GET', 'POST'])
# @login_required
# def register():
#     if request.method == 'POST':
#         hashed_password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256')
#         db.users.insert_one({
#             "email": request.form.get('email'),
#             "username": request.form.get('username'),
#             "password": hashed_password
#         })
#         return redirect(url_for('login'))
#     return render_template('register.html')


#home_page implementation

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/programs')
# @login_required
def programs():
    return render_template('programs.html')

@app.route('/highlights')
# @login_required
def highlights():
    return render_template('highlights.html')


#posts routes
# @app.route('/dashboard')
# # @login_required
# def home():
#     posts = db.posts.find()
#     return render_template('dashboard.html', posts=posts)

#this is to implment the posting feature
# @app.route('/post', methods=['POST'])
# # @login_required
# def post():
#     post_data = request.form['post']
#     db.posts.insert_one({'content' : post_data})
#     return redirect(url_for('home'))

@app.route('/achievements')
# @login_required
def achievements():
    return render_template('achievement.html')

@app.route('/support')
# @login_required
def support():
    return render_template('support.html')


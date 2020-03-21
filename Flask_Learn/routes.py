from flask import Flask,render_template,url_for,flash,redirect
from Flask_Learn.models import User,Post
from Flask_Learn.forms import RegisterationForm,LoginForm
from Flask_Learn import app   # from __init__.py

posts = [
    {
        'author':'Tejoy Vachhrajani',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted' : 'March 9,2020'
    },
    {
        'author':'Jane Doe',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted' : 'March 10,2020'
    }
]

@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title="about")

@app.route("/register",methods=['POST','GET'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !','success')
        return redirect(url_for('home'))
    return render_template('register.html',title="Register",form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in !' ,'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.Please check username and password','danger')
    return render_template('login.html',title="Login",form=form)

from flask import Flask,render_template,url_for,flash,redirect,request
from Flask_Learn.models import User,Post
from Flask_Learn.forms import RegisterationForm,LoginForm
from Flask_Learn import app,db,bcrypt   # from __init__.py
from flask_login import login_user,current_user,logout_user,login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created ! You are now able to log in !','success')
        return redirect(url_for('login'))
    return render_template('register.html',title="Register",form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')        # next parameter query args gets
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.Please check email and password','danger')
    return render_template('login.html',title="Login",form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect (url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html',title='Account')


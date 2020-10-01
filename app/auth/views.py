from . import auth
from .. import db, Bcrypt, photos
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from .forms import SignupForm, LoginForm
from flask_login import login_user,current_user,login_required,logout_user
from ..email import mail_message



@auth.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email =form.email.data).first()
        if user and(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        flash('Invalid username or Password')


    return render_template("auth/login.html",title="Login", form = login_form)  


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if signup_form.validate_on_submit():
        user = User(username=signup_form.username.data, email=signup_form.email.data, password=signup_form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Invalid username or email')


        return redirect(url_for('auth.login'))
    return render_template("auth/signup.html",title="Register", form = signup_form) 

    return  render_template("auth/signup.html") 



    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# @auth.route('/signup', methods = ["GET","POST"])
# def signup():
#     form = SignupForm()
#     if form.validate_on_submit():
#         user = User(email = form.email.data, username = form.username.data, password = form.password.data)
#         user.save_u()
#         mail_message("Welcome to blogcenter","email/welcome_user",user.email,user=current_user)
#         return redirect(url_for('auth.login'))
#     return render_template('auth/signup.html', r_form = form)


# @main.route('/update/pic',methods= ['POST'])

    


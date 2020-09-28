from . import auth
from .. import db, Bcrypt
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from .forms import SignupForm, LoginForm
from flask_login import login_user,current_user,login_required,logout_user


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = SignupForm()
    if form.validate_on_submit():
        # hashed_password = Bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account has been  created,you can log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template("auth/signup.html",title="Register", form = form) 

    return  render_template("auth/signup.html") 



    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email =form.email.data).first()
        if user and(user.password, form.password.data):
        # if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login unsucessful.Please check username and password', 'danger')
    return render_template("auth/login.html",title="Login", form = form)  

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))
    


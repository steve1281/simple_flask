
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect user/password', category='error')
        else:
                flash('Incorrect user/password', category='error')


    return render_template("login.html", boolean=True) # text="Testing String")

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up',methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email used already.',category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.',category='error')
        elif len(firstName) < 2:
            flash('First Name  must be greater than 2 characters.',category='error')
        elif password1 != password2:
            flash('Passwords do not match',category='error')
        elif len(password1) < 4:
            flash("Invalid password.",category='error')
        else:
            new_user = User(email=email, 
                            firstName=firstName, 
                            password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created.",category='success')
            return redirect(url_for('views.home'))

            # add user
    return render_template("sign_up.html")

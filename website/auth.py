from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validate user input
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        # if user exists, check password
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect passord', category='error')
        else:
            flash('User does not exist', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # if request method is POST, then handle information
    if request.method == 'POST':
        # Gather user data
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Validate user data
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Account with email already exists!', category='error')
        elif not email:
            flash('Please enter a valid email.', category='error')
        elif not first_name:
            flash('Please enter a valid name.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error') 
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # Create an account 
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            # Push to database
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    # else (request method must be get) we direct user to sign up
    return render_template("sign_up.html")
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

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
        name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Validate user data
        if not email:
            flash('Please enter a valid email.', category='error')
        elif not name:
            flash('Please enter a valid name.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error') 
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            # Create an account and push to databases
            
            flash('Account created!', category='success')

    # else (request method must be get) we direct user to sign up
    return render_template("sign_up.html")
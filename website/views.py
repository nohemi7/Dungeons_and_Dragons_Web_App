from flask import Blueprint, render_template
from flask_login import login_required, current_user

#Set up blueprint for our flask app
views = Blueprint('views', __name__)

# Routes

# Homepage route
@views.route('/')
@login_required
def home():
    # Display "character sheets"
    return render_template("home.html", user=current_user)

# Character Creator Route
@views.route('/char-creator', methods=['GET', 'POST'])
@login_required
def char_creator():
    return render_template("char_creator.html", user=current_user)
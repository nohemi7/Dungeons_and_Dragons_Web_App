from flask import Blueprint, render_template
from flask_login import login_required, current_user

#Set up blueprint for our flask app
views = Blueprint('views', __name__)

# Routes

# Homepage route
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)
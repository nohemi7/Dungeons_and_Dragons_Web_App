from flask import Blueprint, render_template

#Set up blueprint for our flask app
views = Blueprint('views', __name__)

# Routes

# Homepage route
@views.route('/')
def home():
    return render_template("home.html")
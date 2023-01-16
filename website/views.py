from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Character
from . import db
#Set up blueprint for our flask app
views = Blueprint('views', __name__)

# Global Variables
char_races = [
    "Dragonborn",
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling",
    "Half-Orc",
    "Human",
    "Tiefling"
]
char_classes = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]
char_backgrounds = [
    "Acolyte",
    "Charlatan",
    "Criminal",
    "Entertainer",
    "Folk Hero",
    "Guild Artisan",
    "Hermit",
    "Noble",
    "Outlander",
    "Sage",
    "Sailor",
    "Soldier",
    "Urchin"
]
char_alignments = [
    "Lawful Good",
    "Lawful Neutral",
    "Lawful Evil",
    "Neutral Good",
    "True Neutral",
    "Neutral Evil",
    "Chaotic Good",
    "Chaotic Neutral",
    "Chaotic Evil"
]

# Homepage route
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # TODO: Display "character sheets" with tables
    
    return render_template("home.html", user=current_user)

# Character Creator Route
@views.route('/char-creator', methods=['GET', 'POST'])
@login_required
def char_creator():
    if request.method == 'POST':
        name = request.form.get('char-name')
        race = request.form.get('char-race')
        c_class = request.form.get('char-class')
        background = request.form.get('char-background')
        alignment = request.form.get('char-alignment')

        # Validate Entry
        if not name:
            flash("Name field cannot be empty", category='error')
        elif race not in char_races or c_class not in char_classes or background not in char_backgrounds or alignment not in char_alignments:
            flash("Invalid character input", category='error')
        else:
            # valid input so we update the database of the user to add the character
            # Then redirect to home
            new_character = Character(char_name=name, char_race=race, char_class=c_class, char_background=background, char_alignment=alignment, user_id=current_user.id)
            db.session.add(new_character)
            db.session.commit()
            flash("Character created!", category='success')
            return redirect(url_for("views.home"))
    
    return render_template("char_creator.html", user=current_user, char_races=char_races, 
        char_classes=char_classes, char_backgrounds=char_backgrounds, char_alignments=char_alignments)
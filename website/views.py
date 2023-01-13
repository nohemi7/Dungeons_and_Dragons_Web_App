from flask import Blueprint, render_template
from flask_login import login_required, current_user

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
@views.route('/')
@login_required
def home():
    # Display "character sheets"
    return render_template("home.html", user=current_user)

# Character Creator Route
@views.route('/char-creator', methods=['GET', 'POST'])
@login_required
def char_creator():
    return render_template("char_creator.html", user=current_user, char_races=char_races, 
        char_classes=char_classes, char_backgrounds=char_backgrounds, char_alignments=char_alignments)
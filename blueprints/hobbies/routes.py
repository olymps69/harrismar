from flask import Blueprint, render_template

hobbies_bp = Blueprint('hobbies', __name__, template_folder='templates')

@hobbies_bp.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

from flask import Blueprint, render_template

interests_bp = Blueprint('interests', __name__, template_folder='templates')

@interests_bp.route('/interests')
def interests():
    return render_template('interests.html')

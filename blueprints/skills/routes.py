from flask import Blueprint, render_template

skills_bp = Blueprint('skills', __name__, template_folder='templates')

@skills_bp.route('/skills')
def skills():
    return render_template('skills.html')

from flask import Blueprint, render_template

england_bp = Blueprint('england', __name__, template_folder='templates')

@england_bp.route('/england')
def england():
    return render_template('england.html')

from flask import Blueprint, render_template

greece_bp = Blueprint('greece', __name__, template_folder='templates')

@greece_bp.route('/greece')
def greece():
    return render_template('greece.html')

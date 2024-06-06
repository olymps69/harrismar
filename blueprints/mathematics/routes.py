from flask import Blueprint, render_template

mathematics_bp = Blueprint('mathematics', __name__, template_folder='templates')

@mathematics_bp.route('/mathematics')
def mathematics():
    return render_template('mathematics.html')

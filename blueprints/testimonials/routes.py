from flask import Blueprint, render_template

testimonials_bp = Blueprint('testimonials_bp', __name__, template_folder='templates')

@testimonials_bp.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')
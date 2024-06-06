from flask import Blueprint, render_template
from utils import get_repo_info

home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/')
def home():
    return render_template('index.html')

@home_bp.route('/repo')
def repo_info():
    info = get_repo_info()
    return render_template('repo.html', info=info)

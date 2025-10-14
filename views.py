from flask import Blueprint, render_template

# Define the blueprint
bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/create')
def create():
    return render_template('create.html')


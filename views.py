from flask import Blueprint, render_template, request
bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # Save to DB if needed
        return f"Post created: {title}"
    return render_template('create.html')

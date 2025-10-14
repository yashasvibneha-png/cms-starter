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
        # Here, you can save to database or log
        print(f"New post: {title} - {content}")
        return f"Post '{title}' submitted successfully!"
    return render_template('create.html')

    

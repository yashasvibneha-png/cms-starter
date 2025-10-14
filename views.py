from flask import Blueprint, render_template, request, redirect, url_for

# Define the blueprint
bp = Blueprint('views', __name__)

# In-memory store for posts (for testing)
posts = []

@bp.route('/')
def index():
    return render_template('index.html', posts=posts)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if title and content:
            posts.append({'title': title, 'content': content})
            # Redirect to home page after creating post
            return redirect(url_for('views.index'))

    # For GET request, just show the form
    return render_template('create.html')


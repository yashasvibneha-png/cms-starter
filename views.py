import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from werkzeug.utils import secure_filename

bp = Blueprint('views', __name__)

posts = []  # Temporary in-memory storage

@bp.route('/')
def index():
    return render_template('index.html', posts=posts)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        body = request.form['body']
        image = request.files.get('image')

        filename = None
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        posts.append({
            'title': title,
            'author': author,
            'body': body,
            'image': filename
        })

        return redirect(url_for('views.index'))

    return render_template('create.html')


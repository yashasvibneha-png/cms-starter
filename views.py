from flask import Blueprint, render_template, request, redirect, url_for
import os

bp = Blueprint('views', __name__)
posts = []  # store posts temporarily in memory

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route('/')
def index():
    return render_template('index.html', posts=posts)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        image = request.files['image']

        image_filename = None
        if image and image.filename:
            image_filename = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_filename)

        posts.append({
            'title': title,
            'author': author,
            'content': content,
            'image': image_filename
        })

        return redirect(url_for('views.index'))

    return render_template('create.html')

l_for('views.index'))

   from flask import Blueprint, render_template, request, redirect, url_for
import os

bp = Blueprint('views', __name__)

UPLOAD_FOLDER = 'static/uploads'  # Folder to save uploaded images
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image = request.files['image']

        if image:
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_path)

        # For now, just redirect to home (later you can save title, content, and image_path to database)
        return redirect(url_for('views.index'))

    return render_template('create.html')

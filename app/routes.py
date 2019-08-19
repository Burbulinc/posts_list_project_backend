from flask import render_template, redirect, flash, url_for

from app import app
from app.models import Post


@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html',posts=posts)




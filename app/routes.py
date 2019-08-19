from flask import render_template, redirect, flash, url_for

from app import app
from app.forms import SendPostForm
from app.models import Post


@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    postsForm=SendPostForm()
    return render_template('index.html',posts=posts,form=postsForm)

@app.route('/send_post',methods=['POST'])
def sendPost():
    return "Hello"




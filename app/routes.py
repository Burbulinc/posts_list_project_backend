from flask import render_template, redirect, flash, url_for, request

from app import app, db
from app.forms import SendPostForm
from app.models import Post


@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    postsForm = SendPostForm()
    return render_template('index.html', posts=posts, form=postsForm)


@app.route('/send_post', methods=['POST'])
def sendPost():
    usrname = request.form['username']
    text = request.form['text']

    u = Post(user_name=usrname, text=text)
    db.session.add(u)
    db.session.commit()
    return redirect('/index')

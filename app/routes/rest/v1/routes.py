from flask import jsonify, make_response, abort, request

from app import app, db
from app.models.models import Post


@app.route('/api/v1.0/posts', methods=['GET'])
def get_tasks():
    posts = Post.query.all()
    output = []
    for post in posts:
        user_data = {}
        user_data['id'] = post.id
        user_data['text'] = post.text
        user_data['likes'] = post.likes
        user_data['type'] = post.type
        user_data['user_name'] = post.user_name
        output.append(user_data)
    return jsonify(output)


@app.route('/api/v1.0/posts/<int:task_id>', methods=['GET'])
def get_task(task_id):
    post = Post.query.get(task_id)
    if post is None:
        abort(404)
    user_data = {}
    user_data['id'] = post.id
    user_data['text'] = post.text
    user_data['likes'] = post.likes
    user_data['type'] = post.type
    user_data['user_name'] = post.user_name
    return jsonify(user_data)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1.0/posts', methods=['POST'])
def create_task():
    if request.json:
        username = request.json['user_name']
        text = request.json['text']
    elif request.form:
        username = request.form['user_name']
        text = request.form['text']
    else:
        abort(400)

    post = Post(user_name=username, text=text)
    db.session.add(post)
    db.session.commit()

    user_data = {}
    user_data['id'] = post.id
    user_data['text'] = post.text
    user_data['likes'] = post.likes
    user_data['type'] = post.type
    user_data['user_name'] = post.user_name
    return jsonify(user_data), 201

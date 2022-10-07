import sqlite3
import logging

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

db_connection_counter = 0

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Function to get a total amount of posts in the database
def post_count():
    connection = get_db_connection()
    count = connection.execute('SELECT COUNT(*) FROM posts').fetchone()
    connection.close()
    return count

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    db_connection_counter += 1
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      app.log.info('The article with id "{}" didn\'t find!'.formated(post_id))
      return render_template('404.html'), 404
    else:
      app.log.info('Article "{}" retrieved!'.formated(post.title))
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    app.log.info('About is retrieved!')
    return render_template('about.html')

# Define the Healthcheck endpoint
@app.route('/healthz')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response

# Define the Metrics endpoint
@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"db_connection_count": db_connection_count(), "post_count": db_connection_counter}),
            status=200,
            mimetype='application/json'
    )

    return response

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            app.log.info('Article "{}" created!'.formated(title))

            return redirect(url_for('index'))

    return render_template('create.html')

# start the application on port 3111
if __name__ == "__main__":
   logging.basicConfig(level=logging.DEBUG)
   app.run(host='0.0.0.0', port='3111')
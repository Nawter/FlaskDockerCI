import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
# Set up database connection.
client = MongoClient(
    "mongodb://sampleuser:pass123@ds119020.mlab.com:19020/fladocks")
db = client['fladocks']

@app.route('/')
def todo():
    _items = db.todos.find()
    items = [item for item in _items]
    # Render default page template
    return render_template('index.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    # Save items to database
    db.todos.insert_one(item_doc)

    return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

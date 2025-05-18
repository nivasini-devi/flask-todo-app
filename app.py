from flask import Flask, request, jsonify, render_template
from utils.db import get_db, insert_todo, get_todos, update_todo, delete_todo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def todos():
    return jsonify(get_todos())

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    insert_todo(data)
    return jsonify(data), 201

@app.route('/todos/<id>', methods=['PUT'])
def edit_todo(id):
    data = request.json
    update_todo(id, data)
    return jsonify(data)

@app.route('/todos/<id>', methods=['DELETE'])
def remove_todo(id):
    delete_todo(id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
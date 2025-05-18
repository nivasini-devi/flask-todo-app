from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://nivasinidevi8:PujnrWf5NBtfZpQe@cluster0.2rwgy5s.mongodb.net/')
db = client.todo_db
todos_collection = db.todos

def get_db():
    return todos_collection

def insert_todo(todo):
    todos_collection.insert_one(todo)

def get_todos():
    todos = list(todos_collection.find())
    for todo in todos:
        todo['_id'] = str(todo['_id'])  # Convert ObjectId to string
    return todos

def update_todo(id, todo):
    todos_collection.update_one({'_id': ObjectId(id)}, {'$set': todo})

def delete_todo(id):
    todos_collection.delete_one({'_id': ObjectId(id)})
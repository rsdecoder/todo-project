
from flask import Flask, request, jsonify

app = Flask(__name__)

todoTasks = []
next_id = 1
@app.route('/todos', methods = ['GET'])
def get_todos():
    return jsonify(todoTasks)

# Create a new todo Task
@app.route('/todos', methods = ['POST'])
def create_todo() :
    data = request.get_json()
    global next_id
    todo = {
        'id': next_id,
        'task': data.get('task'),
        'done': False
    }
    todoTasks.append(todo)
    next_id += 1
    return jsonify(todo), 201


# ======================= GET A TODO BY ID =======================
@app.route('/todos/<int:todo_id>', methods = ['GET'])
def get_todo(todo_id):
    todo = (next(t for t in todoTasks if t['id'] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({'error': 'Todo not found'}), 404

# ======================= UPDATE A TODO BY ID ======================
@app.route('/todos/<int:todo_id>', methods = ['PUT'])
def update_todo(todo_id):
    data = request.json()
    todo = next((t for t in todoTasks if t['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    todo['task'] = data.get('task', todo['task'])
    todo['done'] = data.get('done', todo['done'])
    return jsonify(todo)

# ====================== Delete a todo by ID ====================
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todoTasks
    todoTasks = [t for t in todoTasks if t['id'] != todo_id]
    return jsonify({'message': 'Todo deleted'})


if __name__ == '__main__':
    print("Listening to server: ")
    app.run(debug=True)

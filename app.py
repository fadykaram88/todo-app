from flask import Flask, request, jsonify

app = Flask(__name__)

todo_list = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todo_list)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo_list.append(data)
    return jsonify(data), 201

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    if id < len(todo_list):
        todo_list.pop(id)
        return '', 204
    return 'Not Found', 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos=[
   {"label": "My first task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_todo = request.json
    todos.append(new_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):  #(position) es parametro que indica la posición que quiero eliminar de lista
    if position <0 or position>=len(todos):
        return jsonify({"error": "Position no valida"}), 400
    
    del todos[position]
    #print("This is the position to delete:", position)
    return jsonify(todos)
    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
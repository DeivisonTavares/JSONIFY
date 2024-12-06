from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {"id": 1, "name": "Comprar leite", "description": "Ir ao supermercado e comprar leite", "status": "pendente"}
    
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    task['id'] = len(tasks) + 1
    tasks.append(task)
    return jsonify({"message": "Tarefa adicionada com sucesso!", "task": task}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task_status(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['status'] = 'concluída' if task['status'] == 'pendente' else 'pendente'
        return jsonify({"message": "Tarefa atualizada", "task": task})
    return jsonify({"message": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from db import robot_db

app = Flask(__name__)

# Rota para obter todos os robôs
@app.route('/api/robots', methods=['GET'])
def get_robots():
    robots = robot_db.get_all_robots()
    return jsonify(robots)

# Rota para obter um robô específico por ID
@app.route('/api/robots/<int:robot_id>', methods=['GET'])
def get_robot(robot_id):
    robot = robot_db.get_robot_by_id(robot_id)
    if robot:
        return jsonify(robot)
    return jsonify({'message': 'Robot not found'}), 404

# Rota para criar um novo robô
@app.route('/api/robots', methods=['POST'])
def create_robot():
    data = request.json
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    new_robot = robot_db.create_robot(data['name'], data.get('status', 'inactive'))
    return jsonify(new_robot), 201

# Rota para atualizar o status de um robô por ID
@app.route('/api/robots/<int:robot_id>/status', methods=['PUT'])
def update_robot_status(robot_id):
    data = request.json
    if 'status' not in data:
        return jsonify({'error': 'Status is required'}), 400
    
    updated_robot = robot_db.update_robot_status(robot_id, data['status'])
    if updated_robot:
        return jsonify(updated_robot)
    return jsonify({'message': 'Robot not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

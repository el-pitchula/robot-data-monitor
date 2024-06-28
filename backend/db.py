class RobotDB:
    def __init__(self):
        self.robots = [
            {'id': 1, 'name': 'Robot 1', 'status': 'active'},
            {'id': 2, 'name': 'Robot 2', 'status': 'inactive'}
        ]
        self.next_id = 3  # próximo ID disponível para novos robôs

    def get_all_robots(self):
        return self.robots

    def get_robot_by_id(self, robot_id):
        for robot in self.robots:
            if robot['id'] == robot_id:
                return robot
        return None

    def create_robot(self, name, status='inactive'):
        new_robot = {
            'id': self.next_id,
            'name': name,
            'status': status
        }
        self.robots.append(new_robot)
        self.next_id += 1
        return new_robot

    def update_robot_status(self, robot_id, status):
        for robot in self.robots:
            if robot['id'] == robot_id:
                robot['status'] = status
                return robot
        return None

# Instância global do banco de dados (simulando um singleton)
robot_db = RobotDB()

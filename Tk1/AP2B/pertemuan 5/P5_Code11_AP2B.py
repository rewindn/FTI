from flask import Flask, jsonify, request


from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)
# sample data
students = [
    {'id': 1, 'name': 'Rahmad', 'age': 19},
    {'id': 2, 'name': 'Wicaksono', 'age': 22},
    {'id': 3, 'name': 'Adi', 'age': 20}    
]

# GET all students data
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET student data by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = [student for student in students if student['id'] == id]
    return jsonify(student)

# CREATE new student data
@app.route('/students', methods=['POST'])
def create_student():
    student = {
        'id': request.json['id'],
        'name': request.json['name'],
        'age': request.json['age']
    }
    students.append(student)
    return jsonify(student)
    

# UPDATE student data by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = [student for student in students if student['id'] == id]
    student[0]['name'] = request.json['name']
    student[0]['age'] = request.json['age']
    return jsonify(student[0])

# DELETE student data by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = [student for student in students if student['id'] == id]
    students.remove(student[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
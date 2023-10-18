from flask import *

app = Flask(__name__)

# sample data biar gg terdiri dari bnyk objjt
students = [
    {'id': 1, 'name': 'Rahmad', 'age': 19},
    {'id': 2, 'name': 'Wicaksono', 'age': 22},
    {'id': 3, 'name': 'Adi', 'age': 20}
]

# GET all students data
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

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


# GET student data by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = [student for student in students if student['id'] == id]
    return jsonify(student)



app.run(debug=True)
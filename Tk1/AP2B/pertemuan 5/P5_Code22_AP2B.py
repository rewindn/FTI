import requests

# GET all students data
response = requests.get('http://localhost:5000/students')
print('Mengambil Seluruh Data')
print(response.json())
print("==================================")

# GET student data by ID
response = requests.get('http://localhost:5000/students/1')
print('Mengambil Data dengan ID = 1')
print(response.json())
print("==================================")

# CREATE new student data
new_student = {'id': 4, 'name': 'Prastowo', 'age': 21}
response = requests.post('http://localhost:5000/students', json=new_student)
print('Menambahkan Data Baru ke Json')
print(response.json())

# GET all students data after creating new student
response = requests.get('http://localhost:5000/students')
print(response.json())
print("==================================")
# UPDATE student data by ID
update_student = {'name': 'Jordan', 'age': 19}
response = requests.put('http://localhost:5000/students/2', json=update_student)
print('Memperbarui Data pada ID = 2')
print(response.json())

# GET all students data after updating student
response = requests.get('http://localhost:5000/students')
print(response.json())
print("==================================")

# DELETE student data by ID
response = requests.delete('http://localhost:5000/students/3')
print('Menghapus Data dengan ID = 3')
print(response.json())

# GET all students data after deleting student
response = requests.get('http://localhost:5000/students')
print(response.json())


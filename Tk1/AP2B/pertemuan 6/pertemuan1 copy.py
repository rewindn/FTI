
from ast import For
import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMessageBox,QVBoxLayout,QPushButton,QLineEdit,QTextEdit

 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)



class ComplexGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Activity')
        
        label_name = QLabel('Nama:',self)
        label_class = QLabel('Age:',self)
        label_student_id = QLabel('Nomor Induk:',self)

        self.name_input = QLineEdit(self)
        self.class_input = QLineEdit(self)
        self.student_id_input = QLineEdit(self)

        button = QPushButton('Cetak',self)
        button2 = QPushButton('Print From Server',self)
        button.clicked.connect(self.on_button_clicked)
        button2.clicked.connect(self.ketika_diklik)

        self.text_area = QTextEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(label_name)
        layout.addWidget(self.name_input)
        layout.addWidget(label_class)
        layout.addWidget(self.class_input)
        layout.addWidget(label_student_id)
        layout.addWidget(self.student_id_input)
        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(self.text_area)

        self.setLayout(layout)

        self.show()

    def ketika_diklik(self):
        response = requests.get('http://localhost:5000/students')
        print('Mengambil Seluruh Data')
        print(response.json())
        data = ''
        for respon in response.json():
            data += f'\n'
            for row in respon:
                data += f'{row} : {respon[row]}\n'
            self.text_area.setText(data)
                
        
            
        print("==================================")


    # def on_button_clicked(self):
    #     name = self.name_input.text()
    #     student_class = self.class_input.text()
    #     student_id = self.student_id_input.text()

    #     if name and student_class and student_id:
    #         info = f'Nama: {name}\nKelas: {student_class}\nNomor Induk: {student_id}'
    #         self.text_area.setText(info)
    #     else:
    #         QMessageBox.warning(self, 'Peringatan','Silahkan isi semua bidang')

    def on_button_clicked(self):
        name = self.name_input.text()
        age = self.class_input.text()
        id = self.student_id_input.text()

        new_student = {'id': id,'name': name,'age': age,}


        response = requests.post('http://localhost:5000/students', json=new_student)
        print('Menambahkan Data Baru ke Json')
        print(response.json())


        if name and age and id:
            info = f'Nama: {name}\nAge: {age}\nNomor Induk: {id}'
            self.text_area.setText(info)
        else:
            QMessageBox.warning(self, 'Peringatan','Silahkan isi semua bidang')
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ComplexGUI()
    sys.exit(app.exec_())
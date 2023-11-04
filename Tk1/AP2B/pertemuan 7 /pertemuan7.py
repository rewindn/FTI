
import sys
import requests
from PyQt5.QtWidgets import  *

# buat class komplek 
class komplek(QWidget):
    def __init__(self):
        super().__init__()

        # kasih title
        self.setWindowTitle('Activity')
        

        # bikin label untuk bagian 
        label_name = QLabel('Nama:',self)
        label_jk = QLabel('Jenis Kelamin:',self)
        label_class = QLabel('Kelas:',self)
        label_student_id = QLabel('Nomor Induk:',self)
        label_uts = QLabel('Nilai UTS:',self)
        label_uas = QLabel('Nilai UAS:',self)
        

        # bikin input biasa
        self.name_input = QLineEdit(self)
        self.student_id_input = QLineEdit(self)
        self.class_uts_input = QLineEdit(self)
        self.student_uas_input = QLineEdit(self)


        # bikin combobox jk
        self.jk_input = QComboBox(self)
        self.jk_input.addItem(' ') 
        self.jk_input.addItem('laki - laki')
        self.jk_input.addItem('perembipuan')
        

        # bikin combobox kelas
        self.class_input = QComboBox(self)
        self.class_input.addItem(' ') 
        self.class_input.addItem('1IA21') 
        self.class_input.addItem('1IA22') 
        self.class_input.addItem('1IA23') 
        self.class_input.addItem('1IA24') 
        self.class_input.addItem('1IA25') 
        self.class_input.addItem('1IA26') 
        self.class_input.addItem('1IA27') 
        
        
        # bikin button 
        button = QPushButton('Cetak',self)
        button2 = QPushButton('Print From Server',self)
        button.clicked.connect(self.on_button_clicked)
        button2.clicked.connect(self.ketika_diklik)

        # bikin text area
        self.text_area = QTextEdit(self)

        # ngelayout 
        layout = QVBoxLayout()
        layout.addWidget(label_name)
        layout.addWidget(self.name_input)
        layout.addWidget(label_jk);
        layout.addWidget(self.jk_input)
        layout.addWidget(label_class)
        layout.addWidget(self.class_input)
        layout.addWidget(label_student_id)
        layout.addWidget(self.student_id_input)
        layout.addWidget(label_uts)
        layout.addWidget(self.class_uts_input)    
        layout.addWidget(label_uas)
        layout.addWidget(self.student_uas_input)    
        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(self.text_area)
        

        # nambahkan layouy ke apps
        self.setLayout(layout)

        # ngerun
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
        jk = self.jk_input.currentText()
        kelas = self.class_input.currentText()
        id = self.student_id_input.text()
        uts = int(self.class_uts_input.text()) 
        uas = int(self.student_uas_input.text()) 
        
        rata = (uts + uas) / 2

        if rata >= 90:
            nilai = "A"
        elif rata >= 80:
            nilai = "B"
        elif rata >= 70:
            nilai = "C"
        elif rata < 70:
            nilai = "D"
        else:
            nilai = "Eror"



        if name and kelas and id:
            info = f'Nama: {name}\nJenis Kelamin: {jk}\nKelas: {kelas}\nNomor Induk: {id}\nNilai Rata Rata: {rata}\nGrade: {nilai}'
            self.text_area.setText(info)
        else:
            QMessageBox.warning(self, 'Peringatan','Silahkan isi semua bidang')
    

app = QApplication(sys.argv)
gui = komplek()
sys.exit(app.exec_())
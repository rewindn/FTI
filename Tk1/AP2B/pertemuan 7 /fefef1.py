from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Mhs(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        label_nama = QLabel("Nama:")
        label_jk = QLabel("Jenis Kelamin:")
        label_kelas = QLabel("Kelas: ")
        label_npm = QLabel("Nomor Induk:")
        label_uts = QLabel("Nilai UTS:")
        label_uas = QLabel("Nilai UAS:")
        label_nama.setFont(QFont('Arial', 12))

        self.gender_combo = QComboBox()
        self.gender_combo.addItem("Laki Laki")
        self.gender_combo.addItem("Perempuan")
        
        self.kelas_combo = QComboBox()
        self.kelas_combo.addItem("1IA21")
        self.kelas_combo.addItem("1IA22")
        self.kelas_combo.addItem("1IA23")
        self.kelas_combo.addItem("1IA24")
        self.kelas_combo.addItem("1IA25")
        self.kelas_combo.addItem("1IA26")
        self.kelas_combo.addItem("1IA27")
        
        self.input_nama = QLineEdit()
        self.input_npm = QLineEdit()
        self.input_uts = QLineEdit()
        self.input_uas = QLineEdit()
        
        cetak = QPushButton()
        cetak.setText("Cetak")
        cetak.clicked.connect(self.on_clicked)

        self.textArea = QTextEdit()
        
        layout.addWidget(label_nama)
        layout.addWidget(self.input_nama)
        layout.addWidget(label_jk)
        layout.addWidget(self.gender_combo)
        layout.addWidget(label_kelas)
        layout.addWidget(self.kelas_combo)
        layout.addWidget(label_npm)
        layout.addWidget(self.input_npm)
        layout.addWidget(label_uts)
        layout.addWidget(self.input_uts)
        layout.addWidget(label_uas)
        layout.addWidget(self.input_uas)
        layout.addWidget(cetak)
        layout.addWidget(self.textArea)
        
        self.setLayout(layout)
    
    def on_clicked(self):
        nama = self.input_nama.text()
        jk = self.gender_combo.currentText()
        kelas = self.kelas_combo.currentText()
        npm = self.input_npm.text()
        uts = float(self.input_uts.text())
        uas = float(self.input_uas.text())

        
        if nama and npm and jk and kelas and uts and uas:

            rata = (uts + uas) /2
        
            if rata >= 90 and rata <= 100:
                grade = "A"
            elif rata >= 80 and rata < 90:
                grade = "B"
            elif rata >= 70 and rata < 80:
                grade = "C"
            elif rata < 70:
                grade = "D"
            else:
                grade = "Eror"

            info = f'Nama\t: {nama}\nJenis Kelamin\t: {jk}\nKelas\t: {kelas}\nNomor Induk\t: {npm}\nRata-rata\t: {rata}\nGrade\t: {grade}'
            self.textArea.setText(info)
        else:
            QMessageBox.warning(self,"Peringatan","Isi Semua COk")
            


app = QApplication([])
window = Mhs()
window.show()
app.exec()

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import json
class mhs(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self.setFixedSize(900,1000))

        self.setWindowTitle("Data Mahasiswa")

        label_nama = QLabel("Nama")
        label_kelas = QLabel("Kelas")
        label_gender = QLabel("Gender")
        label_npm = QLabel("Npm")
        label_uts = QLabel("UTS")
        label_uas = QLabel("UAS")
        label_jurusan = QLabel("Jurusan")
        label_fakultas = QLabel("Fakultas")

        font = QFont("Arial", 12)  # Membuat font dengan ukuran 12 dan tebal
        label_nama.setFont(font)
        label_kelas.setFont(font)
        label_gender.setFont(font)
        label_npm.setFont(font)
        label_uts.setFont(font)
        label_uas.setFont(font)
        label_jurusan.setFont(font)
        label_fakultas.setFont(font)

        self.input_nama = QLineEdit()
        self.input_npm = QLineEdit()
        self.input_uts = QLineEdit()
        self.input_uas = QLineEdit()
        self.input_jurusan = QLineEdit()
        self.input_fakultas = QLineEdit()

        self.combo_kelas = QComboBox()
        self.combo_kelas.addItem("1IA21")
        self.combo_kelas.addItem("1IA22")
        self.combo_kelas.addItem("1IA23")
        self.combo_kelas.addItem("1IA24")
        self.combo_kelas.addItem("1IA25")
        self.combo_kelas.addItem("1IA26")
        self.combo_kelas.addItem("1IA27")
        self.combo_kelas.addItem("1IA28")
        self.combo_kelas.addItem("1IA29")

        self.combo_gender = QComboBox()
        self.combo_gender.addItem("Laki -  Laki")
        self.combo_gender.addItem("Perempuan")

        cetak = QPushButton()
        cetak.setText("Cetak")
        cetak.clicked.connect(self.on_clicked_cetak)

        hapus = QPushButton()
        hapus.setText("Hapus")
        hapus.clicked.connect(self.on_clicked_hapus)

        self.textarea = QTextEdit()

        layout.addWidget(label_nama)
        layout.addWidget(self.input_nama)
        layout.addWidget(label_kelas)
        layout.addWidget(self.combo_kelas)
        layout.addWidget(label_npm)
        layout.addWidget(self.input_npm)
        layout.addWidget(label_gender)
        layout.addWidget(self.combo_gender)
        layout.addWidget(label_uts)
        layout.addWidget(self.input_uts)
        layout.addWidget(label_uas)
        layout.addWidget(self.input_uas)
        layout.addWidget(label_jurusan)
        layout.addWidget(self.input_jurusan)
        layout.addWidget(label_fakultas)
        layout.addWidget(self.input_fakultas)
        layout.addWidget(cetak)
        layout.addWidget(hapus)
        layout.addWidget(self.textarea)

        self.setLayout(layout)

    def on_clicked_hapus(self):
        self.input_nama.clear()
        self.input_npm.clear()
        self.input_uts.clear()
        self.input_uas.clear()
        self.input_jurusan.clear()
        self.input_fakultas.clear()
        self.combo_gender.setCurrentIndex(0)
        self.combo_kelas.setCurrentIndex(0)

    def on_clicked_cetak(self):
        nama = self.input_nama.text()
        kelas = self.combo_kelas.currentText()
        npm = self.input_npm.text()
        gender = self.combo_gender.currentText()
        uts = self.input_uts.text()
        uas = self.input_uas.text()
        jurusan = self.input_jurusan.text()
        fakultas = self.input_fakultas.text()

        if nama and kelas and npm and gender and uts and uas and jurusan and fakultas :
            if uts.isdigit() and uas.isdigit():
                uts = float(uts)
                uas = float(uas)
                total = (uts * 0.3) + (uas * 0.7)
                grade = ""
                data = {
                    "Nama": nama,
                    "Jenis Kelamin": gender,
                    "Kelas": kelas,
                    "Nomor Induk": npm,
                    "Rata-rata": total,
                    "Grade": grade,
                    "Jurusan": jurusan,
                    "Fakultas": fakultas
                }

                with open("database.json", "a") as file:
                    json.dump(data, file)
                    file.write("\n")

                if uts <= 100 and uas <= 100:
                
                    if total >= 90 and total <= 100:
                        grade = "A"
                    elif total >= 80 and total <= 90:
                        grade = "B"
                    elif total >= 70 and total <= 80:
                        grade = "C"
                    elif total >= 60 and total <= 70:
                        grade = "D"
                    elif total < 60:
                        grade = "E"
                    else:
                        grade = "Error"
                else:
                    grade = "(Error)"
                    total = "(Error)"
                info = f'Nama\t\t: {nama}\nJenis Kelamin\t: {gender}\nKelas\t\t: {kelas}\nNomor Induk\t: {npm}\nRata-rata\t\t: {total}\nGrade\t\t: {grade}\nJurusan\t\t: {jurusan}\nFakultas\t\t: {fakultas}'
                self.textarea.setText(info)
            else:
                QMessageBox.warning(self, "Invalid Input","Tolong masukkan angka ke Nilai UTS dan UAS")
        else:
            QMessageBox.warning(self, "Invalid Input","ISI SEMUA BIDANG")
app = QApplication([])
mhs = mhs()
mhs.show()
app.exec_()
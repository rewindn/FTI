from cProfile import label
from PyQt5.QtWidgets import *
import sys
class komplek(QWidget):
    def __init__(self) :
        super().__init__()
       
        self.setWindowTitle("Kuis");

        self.label = QLabel("Kembalikan Kata Dari Pemograman adalah")
        self.inputan = QLineEdit(self);
        self.button = QPushButton("submit",self);
      
        self.button.clicked.connect(self.pindah)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.inputan)
        layout.addWidget(self.button);
      

        self.setLayout(layout);

        self.show();
        

    def pindah(self):
        name = self.inputan.text()
        if name[::-1] == "pemograman":
            QMessageBox.warning(self, 'Jawaban salah!',' Coba lagi')
        else:
            QMessageBox.information(self,"Jawaban","Jawaban benar!")
    
        
        
        

app = QApplication(sys.argv)
gui = komplek()
sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class inputdialogdemo(QWidget):
    def __init__(self, parent = None):
        super(inputdialogdemo, self).__init__(parent)
        
        layout = QFormLayout()
        self.btn = QPushButton("Choose a Model")
        self.btn.clicked.connect(self.getItem)
        
        self.le = QLineEdit()
        layout.addRow(self.btn,self.le)
        self.btn1 = QPushButton("Choose a MIDI File")
        self.btn1.clicked.connect(self.getFile)
         
        self.le1 = QLineEdit()
        layout.addRow(self.btn1,self.le1)
        self.setLayout(layout)
        self.setWindowTitle("Corpus Prompt")

        self.btn2 = QPushButton("Ok")
        layout.addRow(self.btn2)

        #self.btn2.clicked.connect(self.sendInfo)
        
    def getItem(self):
        items = ("1st-Order Markov Chain", "2nd-Order Markov Chain", "Lempel-Ziv")
        
        item, ok = QInputDialog.getItem(self, "Select Model Dialog", 
            "Available Models:", items, 0, False)
            
        if ok and item:
            self.le.setText(item)

    def getFile(self):
        fname, ok = QFileDialog.getOpenFileName(self, 'Open file', 
           'c:\\',"MIDI files (*.mid)")
        if ok:
            self.le1.setText(str(fname))           

def main(): 
    app = QApplication(sys.argv)
    ex = inputdialogdemo()
    ex.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
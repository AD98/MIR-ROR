import sys
from PyQt5.QtWidgets import *



class Window(QWidget):

  def __init__(self):
    super().__init__()
    self.setGeometry(300, 300, 250, 300)
    self.setWindowTitle('Creative Track')
    #self.add_quit()
    self.add_radio(['button 1', 'button 2'])
    self.add_next()
    self.show()

  """def add_quit(self):
    qbtn = QPushButton("Quit", self)
    qbtn.clicked.connect(self.test)
    qbtn.resize(qbtn.sizeHint())
    qbtn.move(180, 270)"""

  def add_radio(self, labels):
    layout = QVBoxLayout()
    layout.addStretch(1)
    btn_list = []
    for label in labels:
      b = QRadioButton(label)
      layout.addWidget(b)

    self.setLayout(layout)

  def add_next(self):
    btn = QPushButton("Add Note", self)
    #btn.clicked.connect(self.add_note)
    btn.resize(btn.sizeHint())
    btn. move(60, 270)

if (__name__ == '__main__'):
  app = QApplication(sys.argv)
  w = Window()
  #w2 = Window()
  sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import *

if (__name__ == '__main__'):
    a = QApplication(sys.argv)
    w = MainWindow()
    w.move(50, 50)
    w.show()
    sys.exit(a.exec_())

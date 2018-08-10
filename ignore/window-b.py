#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import  QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap

class TrackView (QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox  = QHBoxLayout(self)
        pixmap = QPixmap("./img/TileClouds.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.resize(400, 400)
        self.move(400, 100)
        self.setWindowTitle('Hallow.World')
        self.show()

if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = TrackView()
        sys.exit(app.exec_())

from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from mainwindow_ui import *
from add_track import *
from music21 import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.s = stream.Stream()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
        self.ui.add_track_btn.clicked.connect(self.on_add_track_btn_clicked)

    def on_add_track_btn_clicked(self):
        print('add_track')
        self.add_track = Add_track(self)
        self.add_track.show()

    def on_pushButton_3_clicked(self):
        print('add_note')
        """if (self.ui.note1.isChecked()):
            self.ui.note1.setAutoExclusive(False)
            self.ui.note1.setChecked(False)
            self.ui.note1.setAutoExclusive(True)
            self.ui.track.addWidget(QLabel('1'))
        elif (self.ui.note2.isChecked()):
            self.ui.note2.setAutoExclusive(False)
            self.ui.note2.setChecked(False)
            self.ui.note2.setAutoExclusive(True)
            self.ui.track.addWidget(QLabel('2'))
        elif (self.ui.note3.isChecked()):
            self.ui.note3.setAutoExclusive(False)
            self.ui.note3.setChecked(False)
            self.ui.note3.setAutoExclusive(True)
            self.ui.track.addWidget(QLabel('3'))
        elif (self.ui.random_note.isChecked()):
            self.ui.random_note.setAutoExclusive(False)
            self.ui.random_note.setChecked(False)
            self.ui.random_note.setAutoExclusive(True)
            self.ui.track.addWidget(QLabel('4'))
        else:
            self.ui.track.addWidget(QLabel(self.ui.custom_note.text()))"""
        
        self.s = converter.parse("tinyNotation: d'8 f g a b2 c'4 C c c c1")
        #self.s.write('lily.png', '../img/notes')
        pianoroll = graph.plot.HorizontalBarPitchClassOffset(self.s, colorBackgroundFigure='black')
        pianoroll.figureSize = (3,2)
        pianoroll.colorBackgroundFigure = '#000000'
        pianoroll.colorBackgroundData = '#000000'
        pianoroll.colorGrid = '#111111'
        pianoroll.alpha = 1.0
        pianoroll.colors = ['Cyan']
        pianoroll.doneAction = None
        pianoroll.title = None
        pianoroll.barSpace = 32
        pianoroll.run()
        pianoroll.write('../img/notes.png')
        
        p = QPixmap('../img/notes.png')
        self.ui.label.setPixmap(p)


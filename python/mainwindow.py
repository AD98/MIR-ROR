from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from mainwindow_ui import *
from add_track import *
from music21 import *
<<<<<<< HEAD
from pygame import mixer
import pygame
=======
import numpy as np
>>>>>>> master

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.add_track = None
        self.ui = Ui_MainWindow()
        self.s = stream.Stream()
        self.model_notes = []
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
        self.ui.add_track_btn.clicked.connect(self.on_add_track_btn_clicked)
        pygame.init()
        song = 'nyny.mid'
        mixer.music.load(song)
        self.ui.playButton.clicked.connect(self.playButton_clicked)
        self.ui.pauseButton.clicked.connect(self.pauseButton_clicked)        
        self.ui.note1.setCheckable(False)
        self.ui.note2.setCheckable(False)
        self.ui.note3.setCheckable(False)
        
    def on_add_track_btn_clicked(self):
        print('add_track')
        self.add_track = Add_track(self)
        self.add_track.show()

    def on_pushButton_3_clicked(self):
        print('add_note')
        buttons = [self.ui.note1, self.ui.note2, self.ui.note3, self.ui.random_note, self.ui.custom_note]
        
        to_app = None
        
        for i in range(4):
            if (buttons[i].isChecked()):
                print('here', i)
                buttons[i].setAutoExclusive(False)
                buttons[i].setChecked(False)
                buttons[i].setAutoExclusive(True)
                if (i == 3):
                    to_app = note.Note(np.random.randint(0,128))
                else:
                    to_app = self.model_notes[i]
                break

        if (to_app is None):
            to_app = note.Note(buttons[4].text())
         
        self.s.append(to_app) 
        #self.ui.track.addWidget(QLabel(to_app.nameWithOctave))

        if ((self.add_track is not None) and (self.add_track.model is not None) and (len(self.s) > 1)):
            self.model_notes = num_to_note(self.add_track.model.getBestThree(self.s[-1].pitch.midi))
            for i in range(3):
                if (i < len(self.model_notes)):
                    buttons[i].setCheckable(True)
                    buttons[i].setText(self.model_notes[i].nameWithOctave)
                else:
                    buttons[i].setCheckable(False)
                    t = 'Possible note' + str(i+1)
                    buttons[i].setText(t)


        #self.s = converter.parse("tinyNotation: d'8 f g a b2 c'4 C c c c1")
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

    def playButton_clicked(self):
        print('clicked play')
        mixer.music.play(0)
        #thread = threading.Thread(target=self.updateSlider(), args=())
        #thread.daemon = True
        #thread.start()

    def pauseButton_clicked(self):
        print('clicked pause')
        mixer.music.stop()

def num_to_note(num_list):
    ret = []
    for elem in num_list:
        n = note.Note(elem)
        ret.append(n)
    return ret

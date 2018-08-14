from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from mainwindow_ui import *
from add_track import *
from about import *
from music21 import *
from pygame import mixer
import pygame
import numpy as np

temp_midi = 'temp.mid' # holds data about current track

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.add_track = None
        self.ui = Ui_MainWindow()
        self.s = stream.Stream()
        self.model_notes = []
        self.ui.setupUi(self)

        self.ui.note1.clicked.connect(self.on_note1_clicked)
        self.ui.note2.clicked.connect(self.on_note2_clicked)
        self.ui.note3.clicked.connect(self.on_note3_clicked)
        self.ui.random_note.clicked.connect(self.on_random_note_clicked)
        self.ui.custom_btn.clicked.connect(self.on_custom_btn_clicked)
        self.ui.add_track_btn.clicked.connect(self.on_add_track_btn_clicked)

        self.ui.actionLoad_File.triggered.connect(self.load_file_clicked)
        self.ui.actionAbout.triggered.connect(self.displayAbout)

        # audio backend 
        pygame.init()

        # song preview connections
        self.ui.playButton.clicked.connect(self.playButton_clicked)
        self.ui.pauseButton.clicked.connect(self.pauseButton_clicked)        

        #HACK -- suppress music21 images by feeding nonexistant path
        environment.set('graphicsPath', '/')
        
    def load_file_clicked(self):
        print('browse')
        fname, ok = QFileDialog.getOpenFileName(self, 'Open File','/home', 'MIDI files (*.mid)')
        if ok:
            self.fname = fname
            self.ui.file_label.setText(fname)

    def displayAbout(self):
        print('about')
        self.about = About(self)
        self.about.show()

    def on_add_track_btn_clicked(self):
        print('add_track')
        self.add_track = Add_track(self)
        self.add_track.show()
    

    def on_note1_clicked(self):
        self.add_note(self.ui.note1)
    def on_note2_clicked(self):
        self.add_note(self.ui.note2)
    def on_note3_clicked(self):
        self.add_note(self.ui.note3)
    def on_random_note_clicked(self):
        self.add_note(self.ui.random_note)
    def on_custom_btn_clicked(self):
        self.add_note(self.ui.custom_btn)

    def add_note(self, btn):
        print('add_note ',btn)
        
        to_app = None

        if (btn == self.ui.random_note):
            to_app = note.Note(np.random.randint(0,128))
        elif (btn == self.ui.custom_btn):
            to_app = note.Note(self.ui.custom_note.text())
        else:
            to_app = note.Note(btn.text())
         
        self.s.append(to_app) 
        self.update_btns()
        self.update_track()

    def playButton_clicked(self):
        print('play')
        self.s.write('midi',temp_midi)
        mixer.music.load(temp_midi)
        mixer.music.play(0)
        #thread = threading.Thread(target=self.updateSlider(), args=())
        #thread.daemon = True
        #thread.start()

    def pauseButton_clicked(self):
        print('pause')
        mixer.music.stop()

    def update_track(self):
        print('update_track')
        #self.s = converter.parse("tinyNotation: d'8 f g a b2 c'4 C c c c1")
        #self.s.write('lily.png', '../img/notes')
        pianoroll = graph.plot.HorizontalBarPitchSpaceOffset(self.s, colorBackgroundFigure='black')
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

    def update_btns(self):
        print('update_btns')
        suggestion_btns = [self.ui.note1, self.ui.note2, self.ui.note3]
        if ((self.add_track is not None) and (self.add_track.model is not None) and (len(self.s) >= self.add_track.min_notes)):
            self.model_notes = num_to_note(self.add_track.model.getBestThree(self.s[-1].pitch.midi))
            for i in range(len(suggestion_btns)):
                if (i < len(self.model_notes)):
                    suggestion_btns[i].setEnabled(True)
                    suggestion_btns[i].setText(self.model_notes[i].nameWithOctave)
                else:
                    suggestion_btns[i].setEnabled(False)
                    suggestion_btns[i].setText('Possible Note ' + str(i+1))



def num_to_note(num_list):
    ret = []
    for elem in num_list:
        n = note.Note(elem)
        ret.append(n)
    return ret

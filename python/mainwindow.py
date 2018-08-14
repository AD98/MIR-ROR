from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from mainwindow_ui import *
from add_track import *
from music21 import *
from pygame import mixer
import pygame
import numpy as np

temp_midi = 'temp.mid' # holds data about current track

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tracks = []
        self.cur_track = 0
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
        self.ui.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)
        
        pygame.init()
        self.ui.playButton.clicked.connect(self.playButton_clicked)
        self.ui.pauseButton.clicked.connect(self.pauseButton_clicked)        
        
    def on_add_track_btn_clicked(self):
        print('add_track')
        self.tracks.append(Add_track(self))
        self.tracks[-1].show()
    
    def on_comboBox_currentIndexChanged(self, index):
        self.cur_track = index

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
         
        self.s[self.cur_track].append(to_app) 
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

    def update_btns(self):
        print('update_btns')
        suggestion_btns = [self.ui.note1, self.ui.note2, self.ui.note3]
        if ((len(self.tracks) > self.cur_track) and (self.tracks[self.cur_track].model is not None) and (len(self.s[self.cur_track]) >= self.tracks[self.cur_track].min_notes)):
        #if ((self.add_track is not None) and (self.add_track.model is not None) and (len(self.s) >= self.add_track.min_notes)):
            base_notes = None
            if (isinstance(self.tracks[self.cur_track].model, First_markov)):
                base_notes = self.s[self.cur_track][-1].pitch.midi
            elif (isinstance(self.tracks[self.cur_track].model, Sec_markov)):
                base_notes = [self.s[self.cur_track][len(self.s[self.cur_track]) - 2].pitch.midi, self.s[self.cur_track][-1].pitch.midi]
            self.model_notes = num_to_note(self.tracks[self.cur_track].model.getBestThree(base_notes))
            for i in range(len(suggestion_btns)):
                if (i < len(self.model_notes)):
                    suggestion_btns[i].setEnabled(True)
                    suggestion_btns[i].setText(self.model_notes[i].nameWithOctave)
                else:
                    suggestion_btns[i].setEnabled(False)
                    suggestion_btns[i].setText('Possible Note ' + str(i+1))

    def after_add_track(self):
        self.ui.comboBox.setEnabled(True)
        self.ui.random_note.setEnabled(True)
        self.ui.custom_btn.setEnabled(True)
        self.ui.comboBox.addItem(str(len(self.main_win.tracks)))
        self.ui.comboBox.setCurrentIndex(len(self.main_win.tracks) - 1)
        self.s.append(stream.Part())
        self.update_btns()

def num_to_note(num_list):
    ret = []
    for elem in num_list:
        n = note.Note(elem)
        ret.append(n)
    return ret

# QT 
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtGui import QPixmap

# External
from music21 import *
from pygame import mixer
import pygame
import numpy as np

# Internal
from mainwindow_ui import *
from add_track import *
from about import *
from dialog2 import *
from utils import *

TEMP_MIDI = 'temp.mid' # holds data about current track
LILY_ENABLED = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_variables()
        self.ui.label.setPixmap(QPixmap(''))       

        self.ui.note1.clicked.connect(self.on_note1_clicked)
        self.ui.note2.clicked.connect(self.on_note2_clicked)
        self.ui.note3.clicked.connect(self.on_note3_clicked)
        self.ui.random_note.clicked.connect(self.on_random_note_clicked)
        self.ui.custom_btn.clicked.connect(self.on_custom_btn_clicked)
        self.ui.add_track_btn.clicked.connect(self.on_add_track_btn_clicked)
        self.ui.comboBox_2.currentIndexChanged.connect(self.on_comboBox_2_currentIndexChanged)

        #toolbar buttons
        self.ui.actionLoad_File.triggered.connect(self.load_file_clicked)
        self.ui.actionOptions.triggered.connect(self.save_file_clicked)
        self.ui.actionAbout.triggered.connect(self.displayAbout)
        self.ui.actionNew.triggered.connect(self.new_clicked)

        self.ui.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)

        #view
        self.ui.tabWidget.currentChanged.connect(self.on_change_tab)

        # audio backend 
        pygame.init()

        # song preview connections
        self.ui.playButton.clicked.connect(self.playButton_clicked)
        self.ui.pauseButton.clicked.connect(self.pauseButton_clicked)        

        #HACK -- suppress music21 images by feeding nonexistant path
        platform = common.getPlatform() 
        if platform == 'win':
            environment.set('graphicsPath', 'C:/')
        elif platform == 'darwin': 
            environment.set('graphicsPath', '/usr/bin/true')
        else:
            environment.set('graphicsPath', '/bin/true')

        self.rootfp = getSourceFilePath()


    def load_file_clicked(self):
        print('load button clicked')
        fname, ok = QFileDialog.getOpenFileName(self, 'Open File','/home', 'MIDI files (*.mid)')
        if ok:
            self.load_file(fname)
    
    def load_file(self, fname):
        self.new_clicked()

        # HACK not actually allowing you to change old data
        self.loaded_stream = converter.parse(fname)
        
        self.update_track()
        
    def save_file_clicked(self):
        print('save')
        fname, ok = QFileDialog.getSaveFileName(self, 'Save File','/home', 'MIDI files (*.mid)')
        if ok:
            temp_stream = self.get_stream()
            temp_stream.write('midi', fname)

    def new_clicked(self):
        print('new!')
        self.ui.label.setPixmap(QPixmap(''))
        self.init_variables()
        self.reset_btns()
        self.ui.random_note.setEnabled(False)
        self.ui.custom_btn.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.comboBox.clear()
        self.ui.comboBox_2.setCurrentIndex(0)
        
    def displayAbout(self):
        print('about')
        self.about = About(self)
        self.about.show()

    def on_change_tab(self):
        print('tab change %i' % self.ui.tabWidget.currentIndex())


    def on_add_track_btn_clicked(self):
        print('add_track')
        self.tracks.append(Add_track(self))
        self.tracks[-1].show()
    
    def on_comboBox_currentIndexChanged(self, index):
        print('index changed to ',index)
        if (index < 0):
            return
        self.cur_track = index
        self.reset_btns()
        self.update_btns()

    def on_comboBox_2_currentIndexChanged(self, index):
        self.num_notes = index + 1

    def on_note1_clicked(self):
        if QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
            self.play_note_from_text(self.ui.note1.text())
        else:
            self.add_note(self.ui.note1)
    
    def on_note2_clicked(self):
        if QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
            self.play_note_from_text(self.ui.note2.text())
        else:
            self.add_note(self.ui.note2)
    
    def on_note3_clicked(self):
        if QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
            self.play_note_from_text(self.ui.note3.text())
        else:
            self.add_note(self.ui.note3)
    
    def on_random_note_clicked(self):
        '''if QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
            self.play_note_from_text(self.ui.random_note.text())
        else:
            self.add_note(self.ui.random_note)'''

        self.add_note(self.ui.random_note)
    
    def on_custom_btn_clicked(self):
        if QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
            text = self.ui.custom_note.text()
            if (self.try_catch(text) is None):
                return
            self.play_note_from_text(text)
        else:
            self.add_note(self.ui.custom_btn)

    def add_note(self, btn):
        print('add_note ',btn)

        for i in range(self.num_notes):
            to_app = None
            if (btn == self.ui.random_note):
                if (self.tracks[self.cur_track].chords):
                    to_app = self.get_rn_from_num(np.random.randint(0,14))
                else:
                    to_app = note.Note(np.random.randint(0, 128))
            elif (btn == self.ui.custom_btn):
                text = self.ui.custom_note.text()
                to_app = self.try_catch(text)
                if (to_app is None):
                    return
            else:
                if (btn == self.ui.note1):
                    to_app = self.model_notes[self.cur_track][0]
                elif (btn == self.ui.note2):
                    to_app = self.model_notes[self.cur_track][1]
                elif (btn == self.ui.note3):
                    to_app = self.model_notes[self.cur_track][2]
            
            #Assumes all quarter notes --> magic number is 4
            cur_track_noteCount = len(self.s[self.cur_track].flat.notes)
            if (cur_track_noteCount % 4 == 0):
                self.s[self.cur_track].append(stream.Measure(number=cur_track_noteCount / 4))

            self.s[self.cur_track][-1].append(to_app) 
            self.update_btns(False)
        
        self.update_btns()
        self.update_track()


    def error_msg(self):
        print('error msg')
        self.error = Dialog2(self)
        self.error.show()

    def playButton_clicked(self):
        print('play')
        
        temp_mid_path = str( self.rootfp.joinpath('mid', TEMP_MIDI))
        temp_stream = self.get_stream()
        temp_stream.write('midi',temp_mid_path)
        mixer.music.load(temp_mid_path)

        mixer.music.play(0)
        #thread = threading.Thread(target=self.updateSlider(), args=())
        #thread.daemon = True
        #thread.start()

    def pauseButton_clicked(self):
        print('stopping music')
        mixer.music.stop()

    def update_track(self):
        print('update_track')
        
        #self.s = converter.parse("tinyNotation: d'8 f g a b2 c'4 C c c c1")
        if LILY_ENABLED is True:
            self.s.write('lily.png', self.rootfp.joinpath('img', 'notes.lily'))
            pp = QPixmap(str(self.rootfp.joinpath('img', 'notes.lily.png')))
            self.ui.label_4.setPixmap(pp)

        temp_stream = self.get_stream()

        self.s.show('text')
        pianoroll = graph.plot.HorizontalBarPitchSpaceOffset(temp_stream)
        pianoroll.figureSize = (2,2)
        pianoroll.colorBackgroundData = '#000000'
        pianoroll.colorBackgroundFigure = '#000000'
        pianoroll.colorGrid = '#222211'
        pianoroll.alpha = 1.0
        pianoroll.colors = ['Cyan', '#fc900a', 'yellow', '#abfd00', '#fc0aab', \
                '#fb00ab', '#ef1200', '#bb0222', '#cb10de', '#44dd77', '#4444ff', \
                '#0fbcff' ]
        pianoroll.doneAction = None
        pianoroll.title = None
        pianoroll.barSpace = 32
        pianoroll.hideLeftBottomSpines = True
        pianoroll.run()
        pianoroll.write(str(self.rootfp.joinpath('img', 'notes.png')))
        
        p = QPixmap(str(self.rootfp.joinpath('img', 'notes.png')))
        self.ui.label.setPixmap(p)

    def update_btns(self, change_text=True):
        print('update_btns')
        suggestion_btns = [self.ui.note1, self.ui.note2, self.ui.note3]
        cur_track_notes = self.s[self.cur_track].flat.notes
        if ((len(self.tracks) > self.cur_track) and 
                (self.tracks[self.cur_track].model is not None) and 
                (len(cur_track_notes) >= self.tracks[self.cur_track].min_notes)):
            
            base_notes = None
            cur_track_obj = self.tracks[self.cur_track]

            if (isinstance(cur_track_obj.model, First_markov)):
                if (cur_track_obj.chords):
                    base_notes = chord_to_num[cur_track_notes[-1].figure]
                else:
                    base_notes = cur_track_notes[-1].pitch.midi
            elif (isinstance(cur_track_obj.model, Sec_markov)):
                if (cur_track_obj.chords):
                    base_notes = [chord_to_num[cur_track_notes[len(cur_track_notes) - 2].figure], chord_to_num[cur_track_notes[-1].figure]]
                else:
                    base_notes = [cur_track_notes[len(cur_track_notes) - 2].pitch.midi, cur_track_notes[-1].pitch.midi]

            self.model_notes[self.cur_track] = num_to_note(cur_track_obj.model.getBestThree(base_notes), cur_track_obj.chords, cur_track_obj)
            
            if (change_text):
                for i in range(len(suggestion_btns)):
                    if (i < len(self.model_notes[self.cur_track])):
                        suggestion_btns[i].setEnabled(True)
                        if cur_track_obj.chords:
                            suggestion_btns[i].setText(self.model_notes[self.cur_track][i].figure)
                        else:
                            suggestion_btns[i].setText(self.model_notes[self.cur_track][i].nameWithOctave)
                    else:
                        suggestion_btns[i].setEnabled(False)
                        suggestion_btns[i].setText('Possible Note ' + str(i+1))

    def after_add_track(self):
        self.ui.comboBox.setEnabled(True)
        self.ui.random_note.setEnabled(True)
        self.ui.custom_btn.setEnabled(True)
        self.s.insert(0, stream.Part())
        self.s[-1].append(self.tracks[-1].instrument)
        self.model_notes.append([])
        
        self.ui.comboBox.addItem(str(len(self.tracks)))
        self.ui.comboBox.setCurrentIndex(len(self.tracks) - 1)
        
        self.reset_btns()

    def reset_btns(self):
        suggestion_btns = [self.ui.note1, self.ui.note2, self.ui.note3]
        for i in range(len(suggestion_btns)):
            suggestion_btns[i].setEnabled(False)
            suggestion_btns[i].setText('Possible Note ' + str(i+1))
    
    def init_variables(self):
        self.s = stream.Score()
        self.tracks = []
        self.model_notes = []
        self.cur_track = 0
        self.num_notes = 1
        self.loaded_stream = None

    def get_stream(self):
        ret = stream.Stream()
        ret.insert(0, self.s)
        if (self.loaded_stream is not None):
            ret.insert(0, self.loaded_stream)
        return ret
    
    def get_rn_from_num(self, num):
        rand_rn = num_to_chord[num]
        return roman.RomanNumeral(rand_rn, self.tracks[self.cur_track].key)

    def play_note_from_text(self, n):
        to_play = None
        if (self.tracks[self.cur_track].chords):
            to_play = roman.RomanNumeral(n, self.tracks[self.cur_track].key)
        else:
            to_play = note.Note(n)

        temp_mid_path = str( self.rootfp.joinpath('mid', TEMP_MIDI))
        to_play.write('midi',temp_mid_path)
        mixer.music.load(temp_mid_path)
        mixer.music.play(0)

    def try_catch(self,text):
        to_app = None
        try:
            if (self.tracks[self.cur_track].chords):
                to_app = roman.RomanNumeral(text, self.tracks[self.cur_track].key)
            else:
                to_app = note.Note(text)
            return to_app
        except (pitch.AccidentalException, roman.RomanException):
            self.error_msg()
            print('exception found')
            return None


def num_to_note(num_list, chords, cur_track_obj):
    ret = []
    for elem in num_list:
        n = None
        if (chords):
            n = roman.RomanNumeral(num_to_chord[elem],cur_track_obj.key)
        else:
            n = note.Note(elem)
        ret.append(n)
    return ret


from PyQt5.QtWidgets import QDialog, QInputDialog, QFileDialog
from music21 import *

import sys

from add_track_ui import *
from dialog import *
from models.markov_class import *
from models.lz_class import *
from utils import *

num_to_chord = { 
        0:  'I', 
        1:  'II', 
        2:  'III',
        3:  'IV',
        4:  'V', 
        5:  'VI',
        6:  'VII',
        7:  'i',
        8:  'ii',
        9:  'iii',
        10: 'iv',
        11: 'v',
        12: 'vi',
        13: 'vii'  }

chord_to_num = { 
        'I':    0, 
        'II':   1, 
        'III':  2,
        'IV':   3,
        'V':    4, 
        'VI':   5,
        'VII':  6,
        'i':    7,
        'ii':   8,
        'iii':  9,
        'iv':   10,
        'v':    11,
        'vi':   12,
        'vii':  13  }


def chord_parse(rn):
    str_chord = rn.figure
    ret = ''
    for char in str_chord:
        if (char == 'i') or (char == 'v') or (char == 'I') or (char == 'V'):
            ret += char
    return ret

class Add_track(QDialog):
    def __init__(self, main_win):
        super().__init__()
        self.main_win = main_win
        self.model = None
        self.fname = None
        self.chords = False
        self.min_notes = sys.maxsize
        self.ui = Ui_Add_track()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.ui.buttonBox.accepted.connect(self.on_buttonBox_accepted)
    
    def get_data(self, fname):
        s = converter.parse(fname)
        self.key = s.analyze('key')
        ret = []
        if self.chords:
            s = s.chordify().getElementsByClass('Chord')
            for elem in s:
                dict_key = chord_parse(roman.romanNumeralFromChord(elem, self.key))
                if (dict_key in chord_to_num):
                    ret.append(chord_to_num[dict_key])

        else:
            s = s.flat.notes
            for elem in s:
                if isinstance(elem, note.Note):
                    ret.append(elem.pitch.midi)
                elif isinstance(elem, chord.Chord):
                    if (len(elem.pitches) > 0):
                        ret.append(elem.pitches[0].midi)
        return ret


    def on_pushButton_clicked(self):
        print('browse')
        fname, ok = QFileDialog.getOpenFileName(self, 'Open File','./', 'MIDI files (*.mid)')
        if ok:
            self.fname = fname
            self.ui.file_label.setText(fname)

    def on_buttonBox_accepted(self):
        print('accepted')
        model_str = str(self.ui.comboBox.currentText())

        if (self.fname is None):
            self.error_msg()
            self.fname = getSourceFilePath().joinpath('mid', 'test.mid')

        self.instrument = instrument.fromString(str(self.ui.comboBox_2.currentText()))
        if (str(self.ui.comboBox_3.currentText()) == 'Chords'):
            self.chords = True
        data = self.get_data(self.fname)

        if (model_str == '1st Order Markov Chain') and (self.chords):
            self.model = First_markov(data, 14)
            self.min_notes = 1
        elif (model_str == '2nd Order Markov Chain') and (self.chords):
            self.model = Sec_markov(data, 14)
            self.min_notes = 2
        elif (model_str == '1st Order Markov Chain'):
            self.model = First_markov(data)
            self.min_notes = 1
        elif (model_str == '2nd Order Markov Chain'):
            self.model = Sec_markov(data)
            self.min_notes = 2
        elif (model_str == 'Lempel ziv'):
            self.model = Lz(data)

        self.main_win.after_add_track()
        
    def error_msg(self):
        print('error msg')
        self.error = Dialog(self)
        self.error.show()

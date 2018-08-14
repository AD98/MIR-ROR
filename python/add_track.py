from PyQt5.QtWidgets import QDialog, QInputDialog, QFileDialog
from add_track_ui import *
from music21 import *
from models.markov_class import *
from models.lz_class import *
import sys

def get_data(fname):
    s = converter.parse(fname)
    s = s.flat.notes
    ret = []
    for elem in s:
        if isinstance(elem, note.Note):
            ret.append(elem.pitch.midi)
        elif isinstance(elem, chord.Chord):
            if (len(elem.pitches) > 0):
                ret.append(elem.pitches[0].midi)
    return ret

class Add_track(QDialog):
    def __init__(self, main_win):
        super().__init__()
        self.main_win = main_win
        self.model = None
        self.fname = None
        self.min_notes = sys.maxsize
        self.ui = Ui_Add_track()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.ui.buttonBox.accepted.connect(self.on_buttonBox_accepted)

    def on_pushButton_clicked(self):
        print('browse')
        fname, ok = QFileDialog.getOpenFileName(self, 'Open File','/home', 'MIDI files (*.mid)')
        if ok:
            self.fname = fname
            self.ui.file_label.setText(fname)

    def on_buttonBox_accepted(self):
        print('accepted')
        model_num = self.ui.comboBox.currentIndex()

        ###### remove this line when not testing
        # self.fname = '/Users/anshuldoshi/Downloads/uptown_funk.mid'

        data = get_data(self.fname)
        if (model_num == 0):
            self.model = First_markov(data)
            self.min_notes = 1
        elif (model_num == 1):
            self.model = Sec_markov(data)
            self.min_notes = 2
        elif (model_num == 2):
            self.model = Lz(data)

        self.main_win.after_add_track()
        

from PyQt5.QtWidgets import QDialog, QInputDialog, QFileDialog
from add_track_ui import *
from music21 import *
from models.markov_class import *

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
    def __init__(self,parent):
        super().__init__()
        self.model = None
        self.fname = None
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
        data = get_data(self.fname)
        if (model_num == 1):
            self.model = Lz(data)
        elif (model_num == 2):
            self.model = First_markov(data)
        elif (model_num == 3):
            self.model = Sec_markov(data)

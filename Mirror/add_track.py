from PyQt5.QtWidgets import QDialog, QInputDialog, QFileDialog
from add_track_ui import *

class Add_track(QDialog):
    def __init__(self,parent):
        super().__init__()
        self.ui = Ui_Add_track()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        print('browse')
        fname, ok = QFileDialog.getOpenFileName(self, 'Open File','/home', 'MIDI files (*.mid)')
        if ok:
            self.training_file = fname
            self.ui.file_label.setText(fname)

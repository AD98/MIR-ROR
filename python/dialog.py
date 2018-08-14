from PyQt5.QtWidgets import QDialog, QInputDialog, QFileDialog
from dialog_ui import *

#error message for empty file when adding tracks
class Dialog(QDialog):
    def __init__(self, main_win):
        super().__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
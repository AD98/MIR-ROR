from PyQt5.QtWidgets import QDialog, QInputDialog, QFileDialog
from dialog2_ui import *

#error message for custom note addition
class Dialog2(QDialog):
    def __init__(self, main_win):
        super().__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


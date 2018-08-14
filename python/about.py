from PyQt5.QtWidgets import QDialog, QInputDialog, QFileDialog
from about_ui import *

class About(QDialog):
    def __init__(self, main_win):
        super().__init__()
        
        self.ui = Ui_About()
        self.ui.setupUi(self)
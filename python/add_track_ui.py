# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\cpp\add_track.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add_track(object):
    def setupUi(self, Add_track):
        Add_track.setObjectName("Add_track")
        Add_track.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        Add_track.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Add_track)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Add_track)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 351, 184))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.file_label = QtWidgets.QLabel(self.layoutWidget)
        self.file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_label.setObjectName("file_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.file_label)
        self.cbbox3label = QtWidgets.QLabel(self.layoutWidget)
        self.cbbox3label.setObjectName("cbbox3label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cbbox3label)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_4 = QtWidgets.QLabel(Add_track)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 221, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Add_track)
        self.buttonBox.accepted.connect(Add_track.accept)
        self.buttonBox.rejected.connect(Add_track.reject)
        QtCore.QMetaObject.connectSlotsByName(Add_track)

    def retranslateUi(self, Add_track):
        _translate = QtCore.QCoreApplication.translate
        Add_track.setWindowTitle(_translate("Add_track", "Dialog"))
        self.label.setText(_translate("Add_track", "Choose MIDI:"))
        self.pushButton.setText(_translate("Add_track", "Browse"))
        self.label_2.setText(_translate("Add_track", "Model Type:"))
        self.comboBox.setItemText(0, _translate("Add_track", "1st Order Markov Chain"))
        self.comboBox.setItemText(1, _translate("Add_track", "2nd Order Markov Chain"))
        self.comboBox.setItemText(2, _translate("Add_track", "Lempel ziv"))
        self.label_3.setText(_translate("Add_track", "Instrument:"))
        self.comboBox_2.setItemText(0, _translate("Add_track", "Piano"))
        self.comboBox_2.setItemText(1, _translate("Add_track", "Acoustic Guitar"))
        self.comboBox_2.setItemText(2, _translate("Add_track", "Saxophone"))
        self.comboBox_2.setItemText(3, _translate("Add_track", "Trumpet"))
        self.comboBox_2.setItemText(4, _translate("Add_track", "Violin"))
        self.file_label.setText(_translate("Add_track", "No file selected"))
        self.cbbox3label.setText(_translate("Add_track", "Track Type:"))
        self.comboBox_3.setItemText(0, _translate("Add_track", "Melody"))
        self.comboBox_3.setItemText(1, _translate("Add_track", "Chords"))
        self.label_4.setText(_translate("Add_track", "Choose Options for New Track:"))


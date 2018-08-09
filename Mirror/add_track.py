# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_track.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add_track(object):
    def setupUi(self, Add_track):
        Add_track.setObjectName("Add_track")
        Add_track.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Add_track)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Add_track)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 287, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.label_4 = QtWidgets.QLabel(Add_track)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 221, 31))
        self.label_4.setObjectName("label_4")
        self.file_label = QtWidgets.QLabel(Add_track)
        self.file_label.setGeometry(QtCore.QRect(160, 60, 201, 20))
        self.file_label.setObjectName("file_label")

        self.retranslateUi(Add_track)
        self.buttonBox.accepted.connect(Add_track.accept)
        self.buttonBox.rejected.connect(Add_track.reject)
        QtCore.QMetaObject.connectSlotsByName(Add_track)

    def retranslateUi(self, Add_track):
        _translate = QtCore.QCoreApplication.translate
        Add_track.setWindowTitle(_translate("Add_track", "Dialog"))
        self.label.setText(_translate("Add_track", "Choose MIDI:"))
        self.comboBox.setItemText(0, _translate("Add_track", "<Select Model>"))
        self.comboBox.setItemText(1, _translate("Add_track", "Lempel ziv"))
        self.comboBox.setItemText(2, _translate("Add_track", "1st Order Markov Chain"))
        self.comboBox.setItemText(3, _translate("Add_track", "2nd Order Markov Chain"))
        self.comboBox_2.setItemText(0, _translate("Add_track", "<Select Instrument>"))
        self.comboBox_2.setItemText(1, _translate("Add_track", "Guitar"))
        self.comboBox_2.setItemText(2, _translate("Add_track", "Piano"))
        self.label_2.setText(_translate("Add_track", "Model Type:"))
        self.label_3.setText(_translate("Add_track", "Instrument:"))
        self.pushButton.setText(_translate("Add_track", "Browse"))
        self.label_4.setText(_translate("Add_track", "Choose Options for New Track"))
        self.file_label.setText(_translate("Add_track", "No file selected"))


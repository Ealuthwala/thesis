# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aluthwala\Desktop\imageListItem.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


# class QCustomQWidget (QtGui.QWidget):
#     def __init__ (self, parent = None):
#         super(QCustomQWidget, self).__init__(parent)
#         self.textQVBoxLayout = QtGui.QVBoxLayout()
#         self.textUpQLabel    = QtGui.QLabel()
#         self.textDownQLabel  = QtGui.QLabel()
#         self.textQVBoxLayout.addWidget(self.textUpQLabel)
#         self.textQVBoxLayout.addWidget(self.textDownQLabel)
#         self.allQHBoxLayout  = QtGui.QHBoxLayout()
#         self.iconQLabel      = QtGui.QLabel()
#         self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
#         self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
#         self.setLayout(self.allQHBoxLayout)
#         # setStyleSheet
#         self.textUpQLabel.setStyleSheet('''
#             color: rgb(0, 0, 255);
#         ''')
#         self.textDownQLabel.setStyleSheet('''
#             color: rgb(255, 0, 0);
#         ''')
#
#     def setTextUp (self, text):
#         self.textUpQLabel.setText(text)
#
#     def setTextDown (self, text):
#         self.textDownQLabel.setText(text)
#
#     def setIcon (self, imagePath):
#         self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))


class imageListItem(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal()
    def __init__(self,parent=None):

        super(imageListItem, self).__init__(parent)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.setLayout(self.horizontalLayout)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.parentList = QtWidgets.QListWidget
        self.item = QtWidgets.QListWidgetItem
        self.pushButton.clicked.connect(self.clicked)

    def retranslateUi(self):
        self.label_2.setText( "TextLabel")
        self.label.setText("Un checked")
        self.pushButton.setText( "Remove")

    def initialize(self,name,item, list):
        self.label_2.setText(name)
        self.item = item
        self.parentList = list
        # self.pushButton.clicked.connect(self.removeItem)


    def removeItem(self):
        self.parentList.removeItemWidget(self.item)
        # self.parentList.u





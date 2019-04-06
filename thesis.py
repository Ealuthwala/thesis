# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aluthwala\Desktop\thesis.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import imageListItem
import ntpath
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.PathEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PathEdit.setObjectName("PathEdit")
        self.horizontalLayout_6.addWidget(self.PathEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LoadBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadBtn.sizePolicy().hasHeightForWidth())
        self.LoadBtn.setSizePolicy(sizePolicy)
        self.LoadBtn.setObjectName("LoadBtn")
        self.horizontalLayout_3.addWidget(self.LoadBtn)
        self.BrowseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseBtn.setObjectName("BrowseBtn")
        self.horizontalLayout_3.addWidget(self.BrowseBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.ImageList = QtWidgets.QListWidget(self.centralwidget)
        self.ImageList.setObjectName("ImageList")
        self.verticalLayout.addWidget(self.ImageList)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.TypeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TypeLabel.sizePolicy().hasHeightForWidth())
        self.TypeLabel.setSizePolicy(sizePolicy)
        self.TypeLabel.setObjectName("TypeLabel")
        self.horizontalLayout_4.addWidget(self.TypeLabel)
        self.TypeCombo = QtWidgets.QComboBox(self.centralwidget)
        self.TypeCombo.setObjectName("TypeCombo")
        self.horizontalLayout_4.addWidget(self.TypeCombo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.CheckImagesBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckImagesBtn.sizePolicy().hasHeightForWidth())
        self.CheckImagesBtn.setSizePolicy(sizePolicy)
        self.CheckImagesBtn.setObjectName("CheckImagesBtn")
        self.verticalLayout_3.addWidget(self.CheckImagesBtn)
        self.RunBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RunBtn.sizePolicy().hasHeightForWidth())
        self.RunBtn.setSizePolicy(sizePolicy)
        self.RunBtn.setObjectName("RunBtn")
        self.verticalLayout_3.addWidget(self.RunBtn)
        self.ClearBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClearBtn.sizePolicy().hasHeightForWidth())
        self.ClearBtn.setSizePolicy(sizePolicy)
        self.ClearBtn.setObjectName("ClearBtn")
        self.verticalLayout_3.addWidget(self.ClearBtn)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ImageAreaLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageAreaLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.ImageAreaLabel.setText("")
        self.ImageAreaLabel.setObjectName("ImageAreaLabel")
        self.verticalLayout_2.addWidget(self.ImageAreaLabel)
        self.ResultList = QtWidgets.QListWidget(self.centralwidget)
        self.ResultList.setObjectName("ResultList")
        self.verticalLayout_2.addWidget(self.ResultList)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Path"))
        self.LoadBtn.setText(_translate("MainWindow", "Load"))
        self.BrowseBtn.setText(_translate("MainWindow", "Browse"))
        self.TypeLabel.setText(_translate("MainWindow", "Type"))
        self.CheckImagesBtn.setText(_translate("MainWindow", "Check Images"))
        self.RunBtn.setText(_translate("MainWindow", "Run Classification"))
        self.ClearBtn.setText(_translate("MainWindow", "Clear"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.inputImages = []
        self.CheckImagesBtn.clicked.connect(self.check_images)
        self.BrowseBtn.clicked.connect(self.browse_files)

    @QtCore.pyqtSlot()
    def browse_files(self):
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(None, "Select Images", "",
                                                         "Image Files (*.png *.jpg *jpeg *.bmp)")
        for fileName in files:
            item = QtWidgets.QListWidgetItem(self.ImageList)
            value = imageListItem.imageListItem()
            name = ntpath.basename(fileName)
            value.initialize(str(name),item,self.ImageList)
            value.clicked.connect(self.remove_item)
            item.setSizeHint(value.sizeHint())
            self.ImageList.addItem(item)
            self.ImageList.setItemWidget(item,value)
            self.inputImages.append([fileName,value])


    @QtCore.pyqtSlot()
    def remove_item(self):
        widget = self.sender()
        gp = widget.mapToGlobal(QtCore.QPoint())
        lp = self.ImageList.viewport().mapFromGlobal(gp)
        row = self.ImageList.row(self.ImageList.itemAt(lp))
        t_it = self.ImageList.takeItem(row)
        del t_it


    def check_images(self):

        for image in self.inputImages:
            state = 0
            # state = verifyImageSize(image[0])
            if state ==0:
                image[1].label.setStyleSheet("color: rgb(255, 0, 0)")
                image[1].label.setText("Fail")
            else:
                image[1].label.setStyleSheet("color: rgb(0, 255, 0)")
                image[1].label.setText("Verified")
    # def path_leaf(self,):
    #     head, tail = ntpath.split(path)
    #     return tail or ntpath.basename(head)

    # def removeItem(self):
    #     self.ImageList.removeItemWidget()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


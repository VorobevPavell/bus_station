# Form implementation generated from reading ui file 'dev/delstation.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DelStation(object):
    def setupUi(self, DelStation):
        DelStation.setObjectName("DelStation")
        DelStation.resize(743, 564)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=DelStation)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 90, 471, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.delBusBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.delBusBtn.setObjectName("delBusBtn")
        self.verticalLayout.addWidget(self.delBusBtn)
        self.backBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.backBtn.setObjectName("backBtn")
        self.verticalLayout.addWidget(self.backBtn)
        self.label = QtWidgets.QLabel(parent=DelStation)
        self.label.setGeometry(QtCore.QRect(30, 160, 57, 14))
        self.label.setObjectName("label")

        self.retranslateUi(DelStation)
        QtCore.QMetaObject.connectSlotsByName(DelStation)

    def retranslateUi(self, DelStation):
        _translate = QtCore.QCoreApplication.translate
        DelStation.setWindowTitle(_translate("DelStation", "Удаление станции"))
        self.delBusBtn.setText(_translate("DelStation", "Удалить"))
        self.backBtn.setText(_translate("DelStation", "Назад"))
        self.label.setText(_translate("DelStation", "Станция"))

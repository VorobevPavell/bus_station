# Form implementation generated from reading ui file 'dev/addstation.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Station(object):
    def setupUi(self, Station):
        Station.setObjectName("Station")
        Station.resize(786, 592)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Station)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 120, 531, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.addStationBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.addStationBtn.setObjectName("addStationBtn")
        self.verticalLayout.addWidget(self.addStationBtn)
        self.backBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.backBtn.setObjectName("backBtn")
        self.verticalLayout.addWidget(self.backBtn)
        self.label = QtWidgets.QLabel(parent=Station)
        self.label.setGeometry(QtCore.QRect(30, 90, 139, 219))
        self.label.setObjectName("label")

        self.retranslateUi(Station)
        QtCore.QMetaObject.connectSlotsByName(Station)

    def retranslateUi(self, Station):
        _translate = QtCore.QCoreApplication.translate
        Station.setWindowTitle(_translate("Station", "Добавление станции"))
        self.addStationBtn.setText(_translate("Station", "Добавить"))
        self.backBtn.setText(_translate("Station", "Назад"))
        self.label.setText(_translate("Station", "Название"))
# Form implementation generated from reading ui file 'dev/delroute.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DelRoute(object):
    def setupUi(self, DelRoute):
        DelRoute.setObjectName("DelRoute")
        DelRoute.resize(743, 564)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=DelRoute)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 90, 471, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.delRouteBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.delRouteBtn.setObjectName("delRouteBtn")
        self.verticalLayout.addWidget(self.delRouteBtn)
        self.backBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.backBtn.setObjectName("backBtn")
        self.verticalLayout.addWidget(self.backBtn)
        self.label = QtWidgets.QLabel(parent=DelRoute)
        self.label.setGeometry(QtCore.QRect(30, 160, 57, 14))
        self.label.setObjectName("label")

        self.retranslateUi(DelRoute)
        QtCore.QMetaObject.connectSlotsByName(DelRoute)

    def retranslateUi(self, DelRoute):
        _translate = QtCore.QCoreApplication.translate
        DelRoute.setWindowTitle(_translate("DelRoute", "Удаление рейса"))
        self.delRouteBtn.setText(_translate("DelRoute", "Удалить"))
        self.backBtn.setText(_translate("DelRoute", "Назад"))
        self.label.setText(_translate("DelRoute", "Рейс"))

# Form implementation generated from reading ui file 'dev/untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(701, 478)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 140, 341, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.calcRoutesBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.calcRoutesBtn.setObjectName("calcRoutesBtn")
        self.verticalLayout.addWidget(self.calcRoutesBtn)
        self.backBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.backBtn.setObjectName("backBtn")
        self.verticalLayout.addWidget(self.backBtn)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 57, 14))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 50, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Подсчет рейсов до станций"))
        self.calcRoutesBtn.setText(_translate("Form", "Посчитать рейсы"))
        self.backBtn.setText(_translate("Form", "Назад"))
        self.label_2.setText(_translate("Form", "Станция"))
        self.label_3.setText(_translate("Form", "Кол-во рейсов:"))
        self.label.setText(_translate("Form", "NaN"))
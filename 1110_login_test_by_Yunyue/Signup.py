# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 500)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 340, 500))
        self.widget.setObjectName("widget")
        self.PB_vcode = QtWidgets.QPushButton(self.widget)
        self.PB_vcode.setGeometry(QtCore.QRect(195, 350, 110, 43))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.PB_vcode.setFont(font)
        self.PB_vcode.setObjectName("PB_vcode")
        self.LE_username = QtWidgets.QLineEdit(self.widget)
        self.LE_username.setGeometry(QtCore.QRect(40, 166, 265, 43))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.LE_username.setFont(font)
        self.LE_username.setObjectName("LE_username")
        self.LBP_username = QtWidgets.QLabel(self.widget)
        self.LBP_username.setGeometry(QtCore.QRect(48, 174, 24, 27))
        self.LBP_username.setText("")
        self.LBP_username.setObjectName("LBP_username")
        self.LBP_rpassword = QtWidgets.QLabel(self.widget)
        self.LBP_rpassword.setGeometry(QtCore.QRect(40, 258, 40, 43))
        self.LBP_rpassword.setText("")
        self.LBP_rpassword.setObjectName("LBP_rpassword")
        self.LE_vcode = QtWidgets.QLineEdit(self.widget)
        self.LE_vcode.setGeometry(QtCore.QRect(40, 350, 150, 43))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.LE_vcode.setFont(font)
        self.LE_vcode.setObjectName("LE_vcode")
        self.LBP_phone = QtWidgets.QLabel(self.widget)
        self.LBP_phone.setGeometry(QtCore.QRect(40, 304, 75, 43))
        self.LBP_phone.setText("")
        self.LBP_phone.setObjectName("LBP_phone")
        self.LB_note = QtWidgets.QLabel(self.widget)
        self.LB_note.setGeometry(QtCore.QRect(40, 402, 190, 15))
        self.LB_note.setText("")
        self.LB_note.setObjectName("LB_note")
        self.LBP_password = QtWidgets.QLabel(self.widget)
        self.LBP_password.setGeometry(QtCore.QRect(40, 212, 40, 43))
        self.LBP_password.setText("")
        self.LBP_password.setObjectName("LBP_password")
        self.PB_signup = QtWidgets.QPushButton(self.widget)
        self.PB_signup.setGeometry(QtCore.QRect(40, 422, 265, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.PB_signup.setFont(font)
        self.PB_signup.setObjectName("PB_signup")
        self.LB_logo = QtWidgets.QLabel(self.widget)
        self.LB_logo.setGeometry(QtCore.QRect(40, 40, 265, 111))
        self.LB_logo.setToolTip("")
        self.LB_logo.setText("")
        self.LB_logo.setObjectName("LB_logo")
        self.PB_close = QtWidgets.QPushButton(self.widget)
        self.PB_close.setGeometry(QtCore.QRect(315, 0, 25, 25))
        self.PB_close.setText("")
        self.PB_close.setObjectName("PB_close")
        self.LE_phone = QtWidgets.QLineEdit(self.widget)
        self.LE_phone.setGeometry(QtCore.QRect(115, 304, 190, 43))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.LE_phone.setFont(font)
        self.LE_phone.setObjectName("LE_phone")
        self.LE_password = QtWidgets.QLineEdit(self.widget)
        self.LE_password.setGeometry(QtCore.QRect(80, 212, 225, 43))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.LE_password.setFont(font)
        self.LE_password.setObjectName("LE_password")
        self.LE_rpassword = QtWidgets.QLineEdit(self.widget)
        self.LE_rpassword.setGeometry(QtCore.QRect(80, 258, 225, 43))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.LE_rpassword.setFont(font)
        self.LE_rpassword.setObjectName("LE_rpassword")
        self.PB_return = QtWidgets.QPushButton(self.widget)
        self.PB_return.setGeometry(QtCore.QRect(0, 0, 25, 25))
        self.PB_return.setText("")
        self.PB_return.setObjectName("PB_return")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Signup"))
        self.PB_vcode.setText(_translate("Dialog", "发送验证码"))
        self.PB_signup.setText(_translate("Dialog", "立即注册"))


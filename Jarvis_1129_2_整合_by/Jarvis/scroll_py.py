# coding=utf-8
"""
热词分析群组初步构建
"""

import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QLabel, QApplication,QFrame
from PyQt5.QtCore import *
from scroll import Ui_Form

class GroupLogic(QFrame,Ui_Form):
    def __init__(self, parent=None):
        super(GroupLogic, self).__init__(parent)
        """初始化函数"""
        self.setupUi(self)
        self.retranslateUi(self)
        """初始化窗体"""
        """初始化列表"""
        self.create_element()
        """初始化搜索框"""
        # self.LE_search.setTextMargins(0, 0, 0, 0)
        self.LE_search.setPlaceholderText("搜索")
        self.setStyleSheet('QWidget{background-color: rgb(100,189,220,100)}'
                           'QLineEdit{background-color:rgb(255,255,255,100);border-radius:3px;border-width:0px;}'
                           'QScrollBar{width:2px;}'
                           'QPushButton{background-color: rgb(255,255,255,100);border:1px;}'
                           'QComboBox{border:0px;border-radius:3px;background: rgb(255,255,255,100);}'
                           'QComboBox:editable{background:rgb(255,255,255,100);}')

    def create_element(self):
        """
        给定参数，动态生成全部群组
        :return:
        """
        self.topFiller = QtWidgets.QWidget()
        self.topFiller.setContentsMargins(0,0,0,0)
        for button in range(20):
            self.PB_group=QtWidgets.QPushButton(self.topFiller)
            self.PB_group.resize(270,60)
            # PNG_group=QtGui.QPixmap('./images/search.png')
            self.PB_group.setIcon(QtGui.QIcon(r"./images/search.png"))
            self.PB_group.setText(str(button))
            self.topFiller.setMinimumSize(0, (button+1) * 60)
            self.PB_group.move(0,button*61)

        self.SA_group.setWidget(self.topFiller)
        self.SA_group.setContentsMargins(0, 0, 0, 0)

    def searchgroup(self):
        """
        搜索框搜索指定群组，并显示
        :return:
        """
        pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = GroupLogic()
    ui.show()
    sys.exit(app.exec_())

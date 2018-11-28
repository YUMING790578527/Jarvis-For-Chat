import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from barabove_py import BarLogic

sys.path.append("..")


class Main_Window(QWidget):
    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        # --------------------------主窗体--------------------------------------#
        super(Main_Window, self).__init__(parent)
        self.resize(1000, 650)  # 设置窗口初始位置和大小
        self.center()  # 设置窗口居中
        self.setWindowTitle('Jarvis For Chat')  # 设置窗口标题
        logo = QIcon()  # 设置窗口logo
        logo.addPixmap(QPixmap("Resource/images/weixin1.png"), QIcon.Normal)
        self.setWindowIcon(logo)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置隐藏边框

        # 主窗网格布局，基底
        self.main_layout = QGridLayout(self, spacing=0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)
        # ------------------------上边框--------------------------------------#
        self.bara = BarLogic()
        self.main_layout.addWidget(self.bara,0,0,1,0)

        # ------------------------左边菜单栏--------------------------------------#
        self.LeftTabWidget = QListWidget()
        self.LeftTabWidget.setFixedWidth(180)
        self.LeftTabWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LeftTabWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LeftTabWidget.setFrameShape(QListWidget.NoFrame)
        # 左侧组件设置
        self.left_layout = QVBoxLayout()
        self.LeftTabWidget.setLayout(self.left_layout)  # 将左侧布局（垂直）绑定到左侧组件上
        # 左侧布局
        self.main_layout.addWidget(self.LeftTabWidget, 5, 0)
        self.LeftTabWidget.currentRowChanged.connect(self.display)  # 绑定
        list_str = ['热点分析', '关键词提醒', '群发助手', '单项好友删除']
        for i in range(4):
            self.item = QListWidgetItem(list_str[i], self.LeftTabWidget)  # 左侧选项的添加
            self.item.setSizeHint(QSize(180, 80))
            self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示

        # --------------------左侧菜单栏头像------------------------------------------#
        self.avatar_layout = QGridLayout()
        self.main_layout.addLayout(self.avatar_layout, 1, 0)  #################################

        self.avatar = QtWidgets.QPushButton()
        self.avatar.setFixedSize(QSize(180, 180))
        self.avatar.setIcon(QIcon(r'Resource/images/avatar1.png'))
        self.avatar.setIconSize(QSize(170, 170))
        self.avatar_layout.addWidget(self.avatar, 2, 0, 3, 3)  ##控件名，行，列，占用行数，占用列数，对齐方式###############################
        self.avatar_layout.setAlignment(self.avatar_layout,Qt.AlignRight)

        #self.weixin = QtWidgets.QPushButton()
        #self.weixin.setFixedSize(QSize(45, 45))
        #self.weixin.setIcon(QIcon(r'Resource/images/weixin1.png'))
        #self.avatar_layout.addWidget(self.weixin, 4, 4, 1, 1)  #################################
        #self.avatar_layout.setAlignment(self.weixin, Qt.AlignRight)
        #self.avatar_layout.setAlignment(self.weixin, Qt.AlignBottom)

        # --------------------------右边页面-------------------------------------------#
        # 在QStackedWidget对象中填充了4个子控件
        self.stack = QStackedWidget(self)
        self.right_layout = QGridLayout()
        # self.main_layout.addLayout(self.right_layout,0,5)
        self.stack.setLayout(self.right_layout)  #################################
        self.main_layout.addWidget(self.stack, 1, 1, 14, 14)  #################################
        # self.stack.setMinimumSize(620,600)

        # 创建4个小控件和函数
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()

        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.stack.addWidget(self.stack4)

        """初始化信号槽"""
        self.bara.PB_close.clicked.connect(QApplication.instance().quit)  # 关闭主窗体

    def center(self):  # 设置窗口居中
        self.qr = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center()
        self.qr.moveCenter(self.cp)
        self.move(self.qr.topLeft())

    # 热词分析
    def stack1UI(self):
        # 水平布局
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        """右侧群组列表"""
        from scroll_py import GroupLogic
        group = GroupLogic()
        # self.layout.addWidget(group,1)
        """左侧显示框"""
        self.W_left = QtWidgets.QWidget()
        #垂直布局
        self.W_left_layout = QVBoxLayout()
        self.W_left_layout.setContentsMargins(0, 0, 0, 0)
        # 图片
        self.logo = QPixmap('Resource/images/LOGO.jpg')
        self.l1 = QLabel(self)
        self.l1.setGeometry(0, 0, 150, 150)
        # lbl.setScaledContents (True)  # 让图片自适应label大小
        # self.logo_label.setStyleSheet("border: 2px solid blue")
        self.l1.setPixmap(self.logo)
        self.l2 = QLabel('请在右侧列表中选择你感兴趣的群组及时间段', self)
        self.l3 = QLabel('开启你的【热词分析】之旅~', self)

        # 间隔区
        self.spacer_1 = QtWidgets.QSpacerItem(80, 30, QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        self.spacer_2 = QtWidgets.QSpacerItem(90, 80, QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)

        #添加控件
        self.W_left_layout.addItem(self.spacer_1)
        self.W_left_layout.addWidget(self.l1,0, QtCore.Qt.AlignHCenter)
        self.W_left_layout.addWidget(self.l2, 0, QtCore.Qt.AlignHCenter)
        self.W_left_layout.addWidget(self.l3, 0, QtCore.Qt.AlignHCenter)
        self.W_left_layout.addItem(self.spacer_2)


        self.W_left.setLayout(self.W_left_layout)
        # self.layout.addWidget(self.W_left)
        """加入主体"""
        self.layout.addWidget(self.W_left)
        self.layout.addWidget(group)
        self.stack1.setLayout(self.layout)

    # 关键词提醒
    # --------未完工------------#
    def stack2UI(self):
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.stack2.resize(620, 600)
        self.stack2.setLayout(main_layout)
        buntton = QPushButton('新建关键词')
        # btn = QPushButton
        # btn.setFrameShape
        # buntton.setGeometry(0,300,100,40)
        # buntton.setStyleSheet('backgroud:rgb(33,33,33)'；)
        buntton.setStyleSheet('background: rgb(19,60,85);')
        buntton.setMinimumSize(620, 600)
        main_layout.addWidget(buntton)

    # 群发助手
    def stack3UI(self):
        # 水平布局
        layout = QHBoxLayout()
        # 添加控件到布局中
        layout.addWidget(QLabel('群发助手鸭'))
        self.stack3.setLayout(layout)

    # 单向好友检测
    def stack4UI(self):
        # 水平布局
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        # 图片
        self.logo = QPixmap('Resource/images/one-way-friend/logo.png')
        self.logo_1abel = QLabel(self)
        self.logo_1abel.setGeometry(0, 0, 150, 150)
        # lbl.setScaledContents (True)  # 让图片自适应label大小
        # self.logo_label.setStyleSheet("border: 2px solid blue")
        self.logo_1abel.setPixmap(self.logo)

        # 提示文字
        self.Warning1 = QLabel('该功能有可能导致您的网页版微信被暂时封号！', self)
        self.Warning2 = QLabel()
        self.Warning2.setText(
            "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">请慎重使用!!!!!</span></p></body></html>")
        self.l2 = QLabel('点击【开始检测】→扫描弹出的二维码登录您的微信→耐心等待几分钟', self)
        self.l3 = QLabel('即可在手机端确认您的单向好友！', self)

        # 检测按钮
        self.pushButton = QPushButton(self)
        self.pushButton.setIcon(QIcon(QPixmap('Resource/images/one-way-friend/button.png')))  # icon
        self.pushButton.setText("开始检测")  # text
        # self.pushButton.setShortcut('Ctrl+D')#shortcut key

        # 间隔区
        self.spacer_1 = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Minimum,
                                              QtWidgets.QSizePolicy.Expanding)
        self.spacer_2 = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Minimum,
                                              QtWidgets.QSizePolicy.Expanding)

        # 点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
        self.pushButton.clicked.connect(lambda: self.whichbtn(self.pushButton))

        # 实现单向好友检测
        self.pushButton.clicked.connect(lambda: self.click_Test_OneWayFriends(self.l2))
        self.pushButton.setToolTip("点击开始检测")  # Tool tip

        # 添加控件
        self.layout.addItem(self.spacer_1)
        self.layout.addWidget(self.logo_1abel, 0, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.Warning1, 0, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.Warning2, 0, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.l2, 0, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.l3, 0, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.layout.addItem(self.spacer_2)

        # 设置布局
        self.stack4.setLayout(self.layout)

    def click_Test_OneWayFriends(self, btn):
        import os
        os.system('python One_Way_Friend_Test.py')
        btn.setText("检测完成！请到手机端微信确认您的单向好友")

    def whichbtn(self, btn):
        # 输出被点击的按钮
        print('clicked button is ' + btn.text())

    # __________________单向好友检测___________________#

    def display(self, i):
        # 设置当前可见的选项卡的索引
        self.stack.setCurrentIndex(i)


# ----------------右边页面的类-------------#


#右侧弹窗
class init_R_Window(QWidget):
    def __init__(self, parent=None):
        super(init_R_Window, self).__init__(parent)
        # 隐藏任务栏|去掉边框|顶层显示
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.resize(650, 600)
        self.setStyleSheet("background: white")
        #控制与主窗口大小和位置的一致
        self.tmpHwnd = None
        # 启动定时器检测主窗口的位置和大小
        self.checkTimer = QTimer(self, timeout=self.checkWindow)
        self.checkTimer.start(10)  # 10毫秒比较流畅


    #控制弹窗与主窗口的相对位置和大小
    def checkWindow(self):
        if demo.isMinimized():
            self.hide()
        if not demo.isVisible():
            self.close()
        if not self.isVisible():
            return
        else:
            #固定弹窗与主界面的相对位置
            #print(ex.geometry().x(),ex.geometry().y())
            self.move(demo.geometry().x()+demo.geometry().width()-self.geometry().width(), demo.geometry().y())
            #固定弹窗与主界面的相对大小
            #print(ex.geometry().width(),ex.geometry().height())
            self.resize(820,demo.geometry().height())

    def handle_click(self):
        self.hide()

    def handle_close(self):
        self.close()





# ---------------主函数------------------------#

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # style = open(r"../Qss/MetroUI.qss", "r", encoding='utf-8')
    # style_str = style.read()
    # app.setStyleSheet(style_str)

    demo = Main_Window()
    s = init_R_Window()

    #demo.LeftTabWidget.currentRowChanged.connect(s.handle_click)
    demo.close_signal.connect(demo.close)
    demo.show()

   # s.show()
    sys.exit(app.exec_())

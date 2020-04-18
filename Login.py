import sys
from PyQt5.QtWidgets import QPushButton,QWidget,QLabel,QLineEdit,QApplication,QFrame,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("CityGuard")
        self.resize(300,200)
        myFrame=QFrame(self)
        lbl1=QLabel("用户名",myFrame)
        lbl2=QLabel("密  码",myFrame)
        lbl2.move(0,30)

        self.leUserName=QLineEdit(myFrame)
        self.lePassWord=QLineEdit(myFrame)
        self.leUserName.move(50,0)
        self.lePassWord.move(50,30)
        self.lePassWord.setEchoMode(QLineEdit.Password)

        btnLogin=QPushButton("登录",myFrame)
        btnQuit=QPushButton("退出",myFrame)
        btnLogin.move(0,80)
        btnQuit.move(110,80)
        btnLogin.clicked.connect(self.btnClick)
        btnQuit.clicked.connect(self.btnClick)
        myFrame.move(50,50)
        myFrame.resize(300,300)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.show()

    def btnClick(self):
        source=self.sender()
        if source.text()=="登录":
            QMessageBox.information(self,"消息","用户名"+self.leUserName.text()+" 密码："+self.lePassWord.text(),QMessageBox.Ok)
        elif source.text()=="退出":
            QApplication.instance().exit()

if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./Icon/logo.png'))
    mc=MyClass()
    app.exec_()
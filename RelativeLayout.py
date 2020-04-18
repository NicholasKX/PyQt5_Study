import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QLineEdit,QLabel,QPushButton

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CityGuard")
        self.setGeometry(app.desktop().width()/2-self.width()/2,50,400,300)
        lblCode=QLabel("验证码",self)
        leCode=QLineEdit(self)
        btnCode=QPushButton("验证",self)
        hlayout=QHBoxLayout(self)
        hlayout.addWidget(lblCode)
        hlayout.addWidget(leCode)
        hlayout.addWidget(btnCode)

        vlayout=QVBoxLayout(self)
        vlayout.addStretch()

        self.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    mc=MyClass()
    app.exec_()

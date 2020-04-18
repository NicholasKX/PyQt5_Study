import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMenuBar,QMainWindow,QAction,QMessageBox

class MyClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,200,400,300)
        self.setWindowTitle("SafetyHat Detection")
        mymenu=self.menuBar()
        fileMenu=mymenu.addMenu("文件")
        actNewWindow=QAction("新建",fileMenu)
        fileMenu.addAction(actNewWindow)
        actNewWindow.triggered.connect(self.newWindow)
        recent=fileMenu.addMenu("最近")
        recent.addAction("文件1")
        recent.addAction("文件2")
        recent.addAction("文件3")
        mymenu.addAction("打开")
        mymenu.addAction("调试")
        actHelp=QAction("帮助",self)
        actHelp.triggered.connect(self.popWindow)
        mymenu.addAction(actHelp)

        self.show()

    def popWindow(self):
        msgbox=QMessageBox(QMessageBox.Information,"帮助","欢迎加微信交流\n+vx:17376555811",QMessageBox.Ok,self)
        msgbox.show()
    def newWindow(self):
        mc2.show()

class MyClass2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("城市让生活更美好")


if __name__=="__main__":
    app=QApplication(sys.argv)
    mc=MyClass()
    mc2=MyClass2()
    app.exec_()
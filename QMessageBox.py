import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QPushButton

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CityGuard")
        # self.geometry(300,200,400,300)
        btn=QPushButton("关闭窗体",self)
        btn.move(50,50)
        btn.clicked.connect(self.close)
        self.show()
    def closeEvent(self, event):
        result= QMessageBox.question(self, "提示：", "确定关闭吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            QMessageBox.information(self,"消息","谢谢")


if __name__=="__main__":
    app=QApplication(sys.argv)
    mc=MyClass()
    app.exec_()
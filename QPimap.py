import sys
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QLineEdit,QTextEdit,QLabel,QFileDialog,QPushButton
from PyQt5.QtGui import QPixmap
class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("CityGuard")
        self.setGeometry(300,200,1025, 704)
        picture_info = QFileDialog.getOpenFileName(QWidget(), '选择图片', '',
                                                   'Picture files(*.jpg , *.png)')
        picturename = picture_info[0]
        print(picturename)
        if picturename == '':
            return
        btn = QPushButton("更换",self)
        btn.move(800,650)
        btn.clicked.connect(self.btnClick)
        lbl=QLabel("图片",self)
        lbl2=QLabel("换",self)
        lbl2.setGeometry(330,10,200,200)
        lbl.setGeometry(10,10,300,300)
        lbl.setPixmap(QPixmap(picturename))
        lbl.setScaledContents(True)
        self.show()
    def btnClick(self):
        self.picture_info = QFileDialog.getOpenFileName(self, '选择图片', '',
                                                        'Picture files(*.jpg , *.png)')
        self.picture_name = self.picture_info[0]
        print(self.picture_name)
        if self.picture_name == '':
            return
        self.lbl2.setPixmap(QPixmap(self.picture_name))
        # 拉伸
        self.lbl2.setScaledContents(True)

if __name__=="__main__":
    app=QApplication(sys.argv)
    mc=MyClass()
    app.exec_()
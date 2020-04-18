import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CityGuard")
        lbl=QLabel("城市让生活更美好",self)
        self.resize(400,300)
        self.move(50,50)
        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    dk=app.desktop()
    mf=MyForm()
    mf.move(dk.width()/2-mf.width()/2,dk.height()/2-mf.height()/2)
    app.exec_()

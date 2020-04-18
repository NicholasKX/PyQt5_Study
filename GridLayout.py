import sys
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QLineEdit,QTextEdit,QLabel

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("CityGuard")
        self.setGeometry(300,200,400,300)
        lbltitle=QLabel("Title",self)
        lblauthor=QLabel("Author",self)
        lblcontent=QLabel("Content",self)

        letitle=QLineEdit()
        leauthor=QLineEdit()
        tecontent=QTextEdit()
        grid=QGridLayout(self)
        grid.addWidget(lbltitle, 0, 0)
        grid.addWidget(letitle, 0, 1)

        grid.addWidget(lblauthor, 1, 0)
        grid.addWidget(leauthor, 1, 1)

        grid.addWidget(lblcontent, 2, 0)
        grid.addWidget(tecontent, 2, 1)

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    mc=MyClass()
    app.exec_()
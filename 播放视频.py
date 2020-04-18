import sys
import cv2
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PlayVideo import *


class MainWindow(QDialog,Ui_MainWindow):
    """ Main GUI with two windows

    One window shows the original image, and the other shows the gray image.
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.timer_camera = QTimer()  # 定义定时器
        video = r'D:\YOLO-V3-Tensorflow\keras-yolo3-master\00.mp4'  # 加载视频文件
        self.cap = cv2.VideoCapture(video)
        self.pushButton_start.clicked.connect(self.slotStart)  # 按钮关联槽函数
        self.pushButton_stop.clicked.connect(self.slotStop)

    def slotStart(self):
        """ Slot function to start the progamme
        """

        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)

    def slotStop(self):
        """ Slot function to stop the programme
        """

        self.cap.release()
        self.timer_camera.stop()  # 停止计时器

    def openFrame(self):
        """ Slot function to capture frame and process it
        """

        ret, frame = self.cap.read()
        if (self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.label_frame.width(), self.label_frame.height())
                self.label_frame.setPixmap(QPixmap.fromImage(q_image))

                q_image2 = QImage(gray.data, width, height, width,
                                  QImage.Format_RGB888).scaled(self.label_frame_process.width(),
                                                               self.label_frame_process.height())
                self.label_frame_process.setPixmap(QPixmap.fromImage(q_image2))
            else:
                self.cap.release()
                self.timer_camera.stop()  # 停止计时器
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("logo.png"))
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
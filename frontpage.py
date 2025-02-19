from PySide6.QtCore import Qt, QCoreApplication, QTextStream
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QApplication
from PySide6.QtGui import QAction, QImage,QPixmap
from ui.ui_form import Ui_Widget
from camera.basler_camera import BaslerCamera
from image_processing.image_process import ImageProcess
from utils.config import load_config, save_config, thresh_bg, thresh_pp, ratio, topEdgeDistance, sideEdgeDistance, tolerance

import cv2

class MySideBar(QMainWindow, Ui_Widget, BaslerCamera, ImageProcess):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.displayCamera()
        
        self.ui.pushButton_Calibration.clicked.connect(self.btn_ScreenCalibration)
        self.ui.pushButton_Operation.clicked.connect(self.btn_ScreenOperation)
        self.ui.pushButton_DataLog1.clicked.connect(self.btn_DataLog)
        self.ui.pushButton_DataLog2.clicked.connect(self.btn_DataLog)
        self.ui.pushButton_Start.clicked.connect(self.start)
        self.ui.pushButton_Stop.clicked.connect(self.stop)
        self.ui.pushButton_Reset.clicked.connect(self.reset)
        self.ui.pushButton_OpenCamera.clicked.connect(self.openCamera)
        self.ui.pushButton_StartCalibration.clicked.connect(self.startCalibration)

    def btn_ScreenOperation(self):
        self.ui.stackedWidget_Page.setCurrentIndex(0)

    def btn_ScreenCalibration(self):
        self.ui.stackedWidget_Page.setCurrentIndex(1)
        
    def btn_DataLog(self):
        # self.ui.stackedWidget_Page.setCurrentIndex(2)
        pass
        
    def start(self):
        self.check_pass_fail()
        # self.open_camera()
        # load_config()
        # self.ui.setupUi(self)

    
    def stop(self):
        self.close_camera()
    
    def reset(self):
        pass
    
    def openCamera(self):
        pass
    
    def startCalibration(self):
        pass
    
    def closeEvent(self, event):
        
        pass
    
    def displayCamera(self, image = cv2.imread("showcheck.jpg")):
        if len(image.shape) == 2:
            height, width = image.shape
            bytes_per_line = width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        else:
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển sang định dạng RGB
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Hiển thị QImage trên QLabel
        pixmap = QPixmap.fromImage(q_image)
        
        # Đảm bảo ảnh vừa với QLabel và giữ nguyên tỷ lệ khung hình
        scaled_pixmap1 = pixmap.scaled(self.ui.label_Cam1.size(), Qt.KeepAspectRatio)
        scaled_pixmap2 = pixmap.scaled(self.ui.label_Cam2.size(), Qt.KeepAspectRatio)
        
        self.ui.label_Cam1.setPixmap(scaled_pixmap1)
        self.ui.label_Cam2.setPixmap(scaled_pixmap2)
        
    def ui_get_dimension(self, image = cv2.imread("image.jpg")):
        image_new,p1, p2, p3, p4, p5, p6 = self.get_dimension(image)
        self.displayCamera(self.rotate_image(image_new, 180))
        self.ui.lineEdit_P1.setText(f"{p1:.2f}")
        self.ui.lineEdit_P2.setText(f"{p2:.2f}")
        self.ui.lineEdit_P3.setText(f"{p3:.2f}")
        self.ui.lineEdit_P4.setText(f"{p4:.2f}")
        self.ui.lineEdit_P5.setText(f"{p5:.2f}")
        self.ui.lineEdit_P6.setText(f"{p6:.2f}")
        return p1, p2, p3, p4, p5, p6
        
    def check_pass_fail(self, image = cv2.imread("image.jpg")):
        p1, p2, p3, p4, p5, p6 = self.ui_get_dimension(image)
        if abs(p1 - topEdgeDistance) > tolerance or abs(p2 - topEdgeDistance) > tolerance or abs(p3 - sideEdgeDistance) > tolerance or abs(p4 - sideEdgeDistance) > tolerance or abs(p5 - sideEdgeDistance) > tolerance or abs(p6 - sideEdgeDistance) > tolerance:
            self.ui.label_PassFail.setText("Fail")
            self.ui.label_PassFail.setStyleSheet("color: red;")
        else:
            self.ui.label_PassFail.setText("Pass")
            self.ui.label_PassFail.setStyleSheet("color: green;")
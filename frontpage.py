from PySide6.QtCore import Qt, QCoreApplication, QTextStream, QDate
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QApplication
from PySide6.QtGui import QAction, QImage,QPixmap
from ui.ui_form import Ui_Widget
from camera.basler_camera import BaslerCamera
from image_processing.image_process import ImageProcess
from utils.config import load_config, save_config, thresh_bg, thresh_pp, ratio, topEdgeDistance, sideEdgeDistance, tolerance

import cv2
import time

class MySideBar(QMainWindow, Ui_Widget, BaslerCamera, ImageProcess):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.camera = BaslerCamera(self.ui)
        
        # self.displayCamera()
        # if 
        
        self.ui.pushButton_Calibration.clicked.connect(self.btn_ScreenCalibration)
        self.ui.pushButton_Operation.clicked.connect(self.btn_ScreenOperation)
        self.ui.pushButton_DataLog1.clicked.connect(self.btn_DataLog)
        self.ui.pushButton_DataLog2.clicked.connect(self.btn_DataLog)
        self.ui.pushButton_Start.clicked.connect(self.start)
        self.ui.pushButton_Stop.clicked.connect(self.stop)
        self.ui.pushButton_Reset.clicked.connect(self.reset)
        self.ui.pushButton_OpenCamera.clicked.connect(self.openCamera)
        self.ui.pushButton_StartCalibration.clicked.connect(self.startCalibration)
        
        self.ui.lineEdit_Top.editingFinished.connect(self.save_new_top_edge)
        self.ui.lineEdit_Side.editingFinished.connect(self.save_new_side_edge)
        self.ui.lineEdit_Tolerance.editingFinished.connect(self.save_new_tolerance)
        
        
    def btn_ScreenOperation(self):
        self.ui.stackedWidget_Page.setCurrentIndex(0)

    def btn_ScreenCalibration(self):
        self.ui.stackedWidget_Page.setCurrentIndex(1)
        
    def btn_DataLog(self):
        if not self.camera.is_open:
            print("Camera is not open. Please open the camera first.")
            return
        if not self.camera.is_continuous:
            print("Camera is not grabbing. Please start the camera first.")
            return
        triggler_test = self.detect_object(self.camera.image_camera_basler)
        if triggler_test:
            self.camera.stop_continuous_grabbing()
            # image_test = self.camera.single_shot()
            # if image_test is None:
            #     print("Failed to capture image.")
            #     return
            # cv2.imwrite("image_test.jpg", image_test)
            self.check_pass_fail(self.camera.image_camera_basler)
            #đóng camera đảm bảo xóa hết
            self.camera.close_camera()
        else:
            print("Sai khung hình.")
        
        
    def start(self):
        self.camera.open_camera()
        self.reload_config_values()

    def stop(self):
        self.camera.stop_continuous_grabbing()
        self.camera.close_camera()
    
    def reset(self):
        if not self.camera.is_open:
            self.camera.open_camera()
        self.camera.start_continuous_grabbing()
    
    def openCamera(self):
        im = self.camera.single_shot()
        # cv2.imwrite("img_test1.jpg", im)
    
    def startCalibration(self):
        print("log data...")
        self.reset()
        
    
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
        
    def ui_get_dimension(self, image):
        image_new,p1, p2, p3, p4, p5, p6 = self.get_dimension(image)
        self.displayCamera(image_new)
        self.ui.lineEdit_P1.setText(f"{p1:.2f}")
        self.ui.lineEdit_P2.setText(f"{p2:.2f}")
        self.ui.lineEdit_P3.setText(f"{p3:.2f}")
        self.ui.lineEdit_P4.setText(f"{p4:.2f}")
        self.ui.lineEdit_P5.setText(f"{p5:.2f}")
        self.ui.lineEdit_P6.setText(f"{p6:.2f}")
        return p1, p2, p3, p4, p5, p6
        
    def check_pass_fail(self, image):
        p1, p2, p3, p4, p5, p6 = self.ui_get_dimension(image)
        if abs(p1 - topEdgeDistance) > tolerance or abs(p2 - topEdgeDistance) > tolerance or abs(p3 - sideEdgeDistance) > tolerance or abs(p4 - sideEdgeDistance) > tolerance or abs(p5 - sideEdgeDistance) > tolerance or abs(p6 - sideEdgeDistance) > tolerance:
            self.ui.label_PassFail.setText("Fail")
            self.ui.label_PassFail.setStyleSheet("color: red;")
        else:
            self.ui.label_PassFail.setText("Pass")
            self.ui.label_PassFail.setStyleSheet("color: green;")
            
    def save_new_top_edge(self):
        self.ui.lineEdit_Top.setText(f"{float(self.ui.lineEdit_Top.text()):.2f}")
        save_config("topEdgeDistance", float(self.ui.lineEdit_Top.text()))
        
    def save_new_side_edge(self):
        self.ui.lineEdit_Side.setText(f"{float(self.ui.lineEdit_Side.text()):.2f}")
        save_config("sideEdgeDistance", float(self.ui.lineEdit_Side.text()))
        
    def save_new_tolerance(self):
        self.ui.lineEdit_Tolerance.setText(f"{float(self.ui.lineEdit_Tolerance.text()):.2f}")
        save_config("tolerance", float(self.ui.lineEdit_Tolerance.text()))
        
    def reload_config_values(self):
        global thresh_bg, thresh_pp, ratio, topEdgeDistance, sideEdgeDistance, tolerance
        thresh_bg, thresh_pp, ratio, topEdgeDistance, sideEdgeDistance, tolerance = load_config()
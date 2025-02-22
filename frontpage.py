from PySide6.QtCore import Qt, QCoreApplication, QTextStream, QDate
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QApplication, QMessageBox
from PySide6.QtGui import QAction, QImage,QPixmap
from ui.ui_form import Ui_Widget
from camera.basler_camera import BaslerCamera
from image_processing.image_process import ImageProcess
from utils.config import  load_config, save_config, thresh_bg, thresh_pp, ratio, topEdgeDistance, sideEdgeDistance, tolerance

import cv2
import time
import threading

class MySideBar(QMainWindow, Ui_Widget, BaslerCamera, ImageProcess):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.camera = BaslerCamera(self.ui)
        self.timer_thread = None

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
        pass
        
    def button_checkDimension(self):
        """Check the dimension of the object."""
        if not self.camera.is_open:
            print("Camera is not open. Please open the camera first.")
            return
        if not self.camera.is_continuous:
            print("Camera is not grabbing. Please start the camera first.")
            return
        triggler_test = self.detect_object(self.camera.image_camera_basler)
        if triggler_test:
            self.continuousStop()
            self.check_pass_fail(self.camera.image_camera_basler)
            self.camera.close_camera()
        else:
            print("Sai khung hình.")
        
    def buton_ignore(self):
        """Ignore and continue mode continuous."""
        if not self.camera.is_open:
            self.camera.open_camera()
        self.continuousStart()
     
    def start(self):
        self.camera.open_camera()
        self.reload_config_values()

    def stop(self):
        self.continuousStop()
        self.camera.close_camera()
    
    def reset(self):
        self.buton_ignore()
    
    def openCamera(self):
        pass
    
    def startCalibration(self):
        print("log data...")
        self.reset()
    
    def continuousStop(self):
        self.camera.stop_continuous_grabbing()
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.cancel()
        
    def continuousStart(self):
        self.camera.start_continuous_grabbing()
        self.start_timer_close_camera()
    
    def closeEvent(self, event):
        """Xử lý sự kiện đóng cửa sổ."""
        reply = QMessageBox.question(self, 'Message',
            "Bạn có chắc chắn muốn thoát?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if self.camera.is_open:
                self.stop()  # Dừng chụp liên tục và tắt camera
            event.accept()
        else:
            event.ignore()
    
    def start_timer_close_camera(self):
        """Bắt đầu bộ đếm thời gian để tắt camera sau 2 phút."""
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.cancel()  # Hủy bộ đếm thời gian cũ nếu đang chạy
        
        self.timer_thread = threading.Timer(120, self.stop)  # 120 giây = 2 phút
        self.timer_thread.start()
        print("bat dau dem thoi gian")
    
    def displayCamera(self, image):
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
        exposure_time, gain, frame_rate = self.camera.get_camera_info()
        self.ui.lineEdit_Exposure.setText(f"{exposure_time:.0f}")
        self.ui.lineEdit_Gain.setText(f"{gain:.1f}")
        self.ui.lineEdit_FrameRate.setText(f"{frame_rate:.0f}")
        
        
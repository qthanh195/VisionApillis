from PySide6.QtCore import Qt, QCoreApplication, QTextStream, QDate
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QApplication, QMessageBox, QFileDialog, QInputDialog
from PySide6.QtGui import QAction, QImage,QPixmap
from ui.ui_form import Ui_Widget
from camera.basler_camera import BaslerCamera
from image_processing.image_process import ImageProcess
from utils.config import  load_config, save_config, thresh_bg, thresh_pp, ratio, topEdgeDistance, sideEdgeDistance, tolerance

import cv2
import time
import threading
import sqlite3
import datetime
import pandas as pd

class MySideBar(QMainWindow, Ui_Widget, BaslerCamera, ImageProcess):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.camera = BaslerCamera(self.ui)
        self.timer_thread = None
        self.trigger_start = False

        self.ui.pushButton_Calibration.clicked.connect(self.btn_ScreenCalibration)
        self.ui.pushButton_Operation.clicked.connect(self.btn_ScreenOperation)
        self.ui.pushButton_DataLog1.clicked.connect(self.show_data_log)
        self.ui.pushButton_DataLog2.clicked.connect(self.btn_DataLog)
        self.ui.pushButton_Start.clicked.connect(self.button_start_stop)
        self.ui.pushButton_Skip.clicked.connect(self.buton_skip)
        self.ui.pushButton_SaveData.clicked.connect(self.button_save_data)
        self.ui.pushButton_OpenCamera.clicked.connect(self.button_openCamera)
        self.ui.pushButton_StartCalibration.clicked.connect(self.button_startCalibration)
        self.ui.pushButton_Measure.clicked.connect(self.button_measure)        

        self.ui.lineEdit_Top.editingFinished.connect(self.save_new_top_edge)
        self.ui.lineEdit_Side.editingFinished.connect(self.save_new_side_edge)
        self.ui.lineEdit_Tolerance.editingFinished.connect(self.save_new_tolerance)
        

    
    def btn_ScreenOperation(self): 
        self.ui.stackedWidget_Page.setCurrentIndex(0)

    def btn_ScreenCalibration(self):
        self.ui.stackedWidget_Page.setCurrentIndex(1)
        
    def btn_DataLog(self):
        pass
        
    def button_measure(self):
        """Check the dimension of the object."""
        if not self.camera.is_open:
            print("Camera is not open. Please open the camera first.")
            return
        if not self.camera.is_continuous:
            print("Camera is not grabbing. Please start the camera first.")
            return
        self.ui.pushButton_Measure.setText("Measuring...")
        triggler_test =  self.detect_object(self.camera.image_camera_basler)
        if triggler_test:
            self.check_pass_fail(self.camera.image_camera_basler)
            self.continuousStop()
            self.camera.close_camera()
            self.ui.pushButton_Measure.hide()
            self.ui.pushButton_Skip.show()
            self.ui.pushButton_SaveData.show()
            self.ui.pushButton_Measure.setText("Measure")
        else:
            print("Sai khung hình.")
        
    def buton_skip(self):
        """Ignore and continue mode continuous."""
        self.remeasure()
        
    def button_save_data(self):
        """Save the data."""
        self.ui.pushButton_SaveData.setText("Saving...")
        self.save_data()
        self.remeasure()
        self.ui.pushButton_SaveData.setText("Save Data")
    
    def remeasure(self):
        """Remeasure the object."""
        if not self.camera.is_open:
            self.camera.open_camera()
        self.continuousStart()
        self.ui.pushButton_Skip.hide()
        self.ui.pushButton_SaveData.hide()
        self.ui.pushButton_Measure.show()
        self.ui.label_PassFail.setText("")
        self.ui.lineEdit_P1.setText(f"")
        self.ui.lineEdit_P2.setText(f"")
        self.ui.lineEdit_P3.setText(f"")
        self.ui.lineEdit_P4.setText(f"")
        self.ui.lineEdit_P5.setText(f"")
        self.ui.lineEdit_P6.setText(f"")
        
    def button_start_stop(self):
        if not self.trigger_start:
            self.start()
            self.trigger_start = True
        else:
            self.stop()
            self.trigger_start = False
    
    def start(self):
        # open camera
        # start chup cam lieen tuc
        # start timer
        # load config
        # doi text
        
        self.camera.open_camera()
        self.reload_config_values()
        self.continuousStart()
        self.ui.pushButton_Start.setText("Stop")
        
    def stop(self):
        # stop chup cam lieen tuc
        # stop timer
        # close camera
        # doi text
        
        self.continuousStop()
        self.camera.close_camera()
        self.ui.pushButton_Start.setText("Start")
    
    def button_openCamera(self):
        pass
    
    def button_startCalibration(self):
        print("log data...")
        
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
        
            
    def save_data(self):
        """Save the data."""
        # Lấy ngày hiện tại
        current_date = QDate.currentDate().toString("yyyy_MM_dd")

        # Tên bảng dựa trên ngày hiện tại
        table_name = f"measurements_{current_date}"

        # Dữ liệu cần lưu
        # data = (
        #     current_date,
        
        #     float(1.5),
        #     float(2.5),
        #     float(1.0),
        #     float(1.5),
        #     float(2.5),
        #     float(3.5),
        #     float(4.5),
        #     float(5.5),
        #     float(6.5),
        #     str("Pass")
        # )
        data = (
            current_date,
            float(self.ui.lineEdit_Serial.text()),
            float(self.ui.lineEdit_Top.text()),
            float(self.ui.lineEdit_Side.text()),
            float(self.ui.lineEdit_Tolerance.text()),
            float(self.ui.lineEdit_P1.text()),
            float(self.ui.lineEdit_P2.text()),
            float(self.ui.lineEdit_P3.text()),
            float(self.ui.lineEdit_P4.text()),
            float(self.ui.lineEdit_P5.text()),
            float(self.ui.lineEdit_P6.text()),
            str(self.ui.label_PassFail.text())
        )

        # Lưu dữ liệu vào SQLite
        try:
            conn = sqlite3.connect('./database/data.db')
            cursor = conn.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    serial_number TEXT,
                    top_edge REAL,
                    side_edge REAL,
                    tolerance REAL,
                    p1 REAL,
                    p2 REAL,
                    p3 REAL,
                    p4 REAL,
                    p5 REAL,
                    p6 REAL,
                    pass_fail TEXT
                )
            ''')
            cursor.execute(f'''
                INSERT INTO {table_name} (date, serial_number, top_edge, side_edge, tolerance, p1, p2, p3, p4, p5, p6, pass_fail)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', data)
            conn.commit()
            # Kiểm tra và xóa các bảng cũ nếu số lượng bảng vượt quá 14
            self.cleanup_old_tables(cursor)
            conn.close()
            print("Dữ liệu đã được lưu vào cơ sở dữ liệu SQLite.")
        except Exception as e:
            print(f"Lỗi khi lưu dữ liệu: {e}")

    def cleanup_old_tables(self, cursor):
        """Xóa các bảng cũ nếu số lượng bảng vượt quá giới hạn."""
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'measurements_%';")
        tables = cursor.fetchall()
        if len(tables) > 14:
            # Sắp xếp các bảng theo thứ tự ngày từ cũ đến mới
            tables_sorted = sorted(tables, key=lambda x: x[0])
            # Xóa các bảng cũ nhất cho đến khi số lượng bảng còn lại là 14
            for table in tables_sorted[:-14]:
                cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")
                print(f"Bảng {table[0]} đã bị xóa.")
    
    def show_data_log(self):
        """Hiển thị danh sách các ngày có dữ liệu."""
        try:
            conn = sqlite3.connect('./database/data.db')
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'measurements_%';")
            tables = cursor.fetchall()
            conn.close()

            # Hiển thị danh sách các bảng (ngày) cho người dùng chọn
            dates = [table[0].replace("measurements_", "") for table in tables]
            date, ok = QInputDialog.getItem(self, "Select data", "Date:", dates, 0, False)
            if ok and date:
                self.export_data_to_excel(date)
        except Exception as e:
            print(f"Lỗi khi truy vấn danh sách các bảng: {e}")

    def export_data_to_excel(self, date):
        """Xuất dữ liệu ra file Excel."""
        table_name = f"measurements_{date}"

        # Đọc dữ liệu từ SQLite
        try:
            conn = sqlite3.connect('./database/data.db')
            df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
            conn.close()

            # Chọn vị trí lưu file Excel
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Lưu file Excel", f"data_{date}.xlsx", "Excel Files (*.xlsx);;All Files (*)", options=options)
            if file_name:
                df.to_excel(file_name, index=False)
                print(f"Dữ liệu đã được xuất ra file {file_name}")
        except Exception as e:
            print(f"Lỗi khi xuất dữ liệu ra file Excel: {e}")
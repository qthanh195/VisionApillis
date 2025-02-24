from pypylon import pylon
import cv2
import threading
import queue
import numpy as np

from utils.config import thresh_bg, thresh_pp, ratio
from image_processing.image_process import ImageProcess
from ui.ui_form import Ui_Widget
from PySide6.QtGui import QAction, QImage,QPixmap
from PySide6.QtCore import Qt, QCoreApplication, QTextStream, QDate

        
class BaslerCamera():
    def __init__(self, ui_widget):
        self.camera = None
        self.is_open = False
        self.is_continuous = False
        self.grab_thread = None
        self.image_camera_basler = None
        self.ui_widget = ui_widget

    def setup_camera(self):
        """Thiết lập cấu hình camera."""
        
        self.camera.PixelFormat.Value = "Mono8" # Đặt định dạng pixel thành Mono8
        self.camera.ExposureAuto.Value = "Continuous" ## Đặt chế độ tự động điều chỉnh độ sáng thành Once
        self.camera.BalanceWhiteAuto.Value = "Continuous" # Đặt chế độ tự động điều chỉnh màu trắng thành Once
        # self.print_camera_settings()
        
    def open_camera(self):
        """Mở camera Basler."""
        try:
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.camera.Open()
            self.is_open = True
            print("Camera đã mở.")
            self.setup_camera()
        except Exception as e:
            print(f"Lỗi khi mở camera: {e}")

    def close_camera(self):
        """Đóng camera Basler."""
        if self.is_open:
            if self.is_continuous:
                self.stop_continuous_grabbing()
            self.camera.Close()
            self.is_open = False
            print("Camera đã đóng.")

    def single_shot(self):
        """Chụp một hình ảnh."""
        if not self.is_open:
            print("Camera chưa được mở.")
            return

        try:
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            grab_result = self.camera.RetrieveResult(490, pylon.TimeoutHandling_ThrowException)

            if grab_result.GrabSucceeded():
                # Chuyển đổi hình ảnh sang định dạng OpenCV
                img = grab_result.Array
                grab_result.Release()
                return img 
            else:
                print("Lỗi khi chụp hình.")
        except Exception as e:
            print(f"Lỗi khi chụp hình: {e}")

    def start_continuous_grabbing(self):
        """Bắt đầu chế độ chụp liên tục."""
        if not self.is_open:
            print("Camera chưa được mở.")
            return
        if self.is_continuous:
            print("Camera đang ở chế độ chụp liên tục.")
            return
        self.is_continuous = True

        def grab_images():
            count_frame = 0
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            while self.is_continuous:
                grab_result = self.camera.RetrieveResult(490, pylon.TimeoutHandling_ThrowException)

                if grab_result.GrabSucceeded():
                    # Chuyển đổi hình ảnh sang định dạng OpenCV
                    self.image_camera_basler = grab_result.Array
                    self.displayCamera()
                    count_frame += 1
                    if count_frame % 16 == 0:
                        self.check_position()
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        break
                    
                grab_result.Release()

            self.camera.StopGrabbing()
            cv2.destroyAllWindows()

        # Kiểm tra và dừng luồng cũ nếu đang chạy
        if self.grab_thread and self.grab_thread.is_alive():
            self.stop_continuous_grabbing()

        self.grab_thread = threading.Thread(target=grab_images)
        self.grab_thread.start()

    def stop_continuous_grabbing(self):
        """Dừng chế độ chụp liên tục."""
        if self.is_continuous:
            self.is_continuous = False
            self.grab_thread.join()
            print("Dừng chụp liên tục.")

    def get_camera_info(self):
        """Lấy thông tin camera."""
        if not self.is_open:
            print("Camera chưa được mở.")
            return

        try:
            exposure_time = self.camera.ExposureTime.Value
            gain =  self.camera.Gain.Value
            frame_rate = self.camera.AcquisitionFrameRate.Value
            return  exposure_time, gain, frame_rate
        except Exception as e:
            print(f"Lỗi khi lấy thông tin camera: {e}")
            
    def print_camera_settings(self):
        """In ra các thông số của camera."""
        try:
            print(f"Pixel Format: {self.camera.PixelFormat.Value}")
            print(f"Exposure Time: {self.camera.ExposureTime.Value}")
            print(f"Balance White Auto: {self.camera.BalanceWhiteAuto.Value}")
            print(f"Gain: {self.camera.Gain.Value}")
            print(f"Gamma: {self.camera.Gamma.Value}")
            print(f"Frame Rate: {self.camera.AcquisitionFrameRate.Value}")
        except Exception as e:
            print(f"Lỗi khi in thông số camera: {e}")

    def check_position(self):
        triggler_capture = ImageProcess().detect_object(self.image_camera_basler)
        if triggler_capture:
            self.ui_widget.frame_Cam1.setStyleSheet("border: 3px solid green;")
        else:
            self.ui_widget.frame_Cam1.setStyleSheet("border: 3px solid red;")
            
    def displayCamera(self):
        image,_ = ImageProcess().rotate_image(self.image_camera_basler, 180)
        crop_width, crop_height = 3800, 2290
        if len(image.shape) == 2:
            height, width = image.shape
            # Tính toán toạ độ crop (ép kiểu int)
            x1 = int((width - crop_width) / 2)
            y1 = int((height - crop_height) / 2)
            x2 = x1 + crop_width
            y2 = y1 + crop_height

            # Cắt ảnh
            image = image[y1-100:y2-100, x1:x2]
            height, width = image.shape
            bytes_per_line = width
            image = np.ascontiguousarray(image)  # Đảm bảo mảng là liên tục trong bộ nhớ
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        else:
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển sang định dạng RGB
            height, width, channel = frame.shape
            # Tính toán toạ độ crop (ép kiểu int)
            x1 = int((width - crop_width) / 2)
            y1 = int((height - crop_height) / 2)
            x2 = x1 + crop_width
            y2 = y1 + crop_height

            # Cắt ảnh
            image = image[y1-100:y2-100, x1:x2]
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            image = np.ascontiguousarray(image)  # Đảm bảo mảng là liên tục trong bộ nhớ
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Hiển thị QImage trên QLabel
        pixmap = QPixmap.fromImage(q_image)
        
        # Đảm bảo ảnh vừa với QLabel và giữ nguyên tỷ lệ khung hình
        scaled_pixmap1 = pixmap.scaled(self.ui_widget.label_Cam1.size(), Qt.KeepAspectRatio)
        scaled_pixmap2 = pixmap.scaled(self.ui_widget.label_Cam2.size(), Qt.KeepAspectRatio)
        
        self.ui_widget.label_Cam1.setPixmap(scaled_pixmap1)
        self.ui_widget.label_Cam2.setPixmap(scaled_pixmap2)
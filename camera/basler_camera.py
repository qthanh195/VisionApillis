from pypylon import pylon
import cv2
import threading

from utils.config import thresh_bg, thresh_pp, ratio
from image_processing.image_process import ImageProcess, detect, handle_stream, handle_stream_with_flag

# thresh_bg, thresh_pp, ratio = Config.thresh_bg, Config.thresh_pp, Config.ratio

class BaslerCamera:
    def __init__(self):
        self.camera = None
        self.is_open = False
        self.is_continuous = False
        self.grab_thread = None
        self.setup_camera()

    def setup_camera(self):
        """Thiết lập cấu hình camera."""
        
        self.open_camera()
        
        self.camera.PixelFormat.Value = "Mono8" # Đặt định dạng pixel thành Mono8
        self.camera.ExposureAuto.Value = "Once" ## Đặt chế độ tự động điều chỉnh độ sáng thành Once
        self.camera.BalanceWhiteAuto.Value = "Once" # Đặt chế độ tự động điều chỉnh màu trắng thành Once
        self.print_camera_settings()
        
    def open_camera(self):
        """Mở camera Basler."""
        try:
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
            self.camera.Open()
            self.is_open = True
            print("Camera đã mở.")
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
            img_new_resized = None
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            while self.is_continuous:
                grab_result = self.camera.RetrieveResult(490, pylon.TimeoutHandling_ThrowException)

                if grab_result.GrabSucceeded():
                    # Chuyển đổi hình ảnh sang định dạng OpenCV
                    img = grab_result.Array
                    img_resized = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)
                    cv2.imshow("Continuous Grab", img_resized)
                    if img_new_resized is not None:
                        cv2.imshow("Img dimension", img_new_resized)

                    # Thoát chế độ chụp liên tục khi nhấn phím 'q'
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        break
                    if key == ord('s'):
                        print("single shot")
                        circles = detect(img, thresh_bg, thresh_pp)
                        if circles:
                            img_process = ImageProcess(img, thresh_bg, thresh_pp)
                            img_process.dimension()
                            img_new = cv2.imread("./Image/test222.jpg")
                            img_new_resized = cv2.resize(img_new, (0, 0), fx=0.4, fy=0.4)
                        else:
                            print(" Không có vật")
                            img_new_resized = None
                    
                grab_result.Release()

            self.camera.StopGrabbing()
            cv2.destroyAllWindows()

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
            info = self.camera.GetDeviceInfo()
            print(f"Tên thiết bị: {info.GetModelName()}")
            print(f"Số sê-ri: {info.GetSerialNumber()}")
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

import cv2
import numpy as np

class Calibration:
    
    def detect_square(self, image):
        if len(image.shape) == 2:
            gray = image 
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(gray, 149, 255, cv2.THRESH_BINARY)
        thresh = cv2.blur(thresh, (3, 3), 2)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            # print(area)
            if 3450000 < area < 3550000:
                print(area)
                return cnt, True
        return None, False
    
    def calibrate(self, image):
        """ Calibrate the camera using the image of the calibration pattern."""
        cnt,_ = self.detect_square(image)
        if cnt is None:
            message = "Calibration failed. The camera distance is incorrect."
            return None, message
        
        # Tìm hình chữ nhật nhỏ nhất bao quanh cnt
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int32(box)
        
        # Tính độ dài các cạnh của hình chữ nhật
        edge_lengths = self.calculate_edge_lengths(box)
        # print("Edge lengths:", edge_lengths)
        edge_min = min(edge_lengths)
        edge_max = max(edge_lengths)
        if edge_max - edge_min > 5:
            message = "Calibration failed. The camera is installed at an angle."
            return None, message
        
        adge_avg = sum(edge_lengths) / 4
        print("Edge average:", adge_avg)
        
        
        # adge_avg pixel = 149.5 mm -> 1 pixel = 149.5 / adge_avg mm
        ratio = 161.3588 / adge_avg
        print("Rato:", ratio)
        message = "Calibration successful."
        return ratio, message

    def calculate_edge_lengths(self, box):
        """Tính độ dài các cạnh của hình chữ nhật."""
        edge_lengths = []
        for i in range(4):
            p1 = box[i]
            p2 = box[(i + 1) % 4]
            edge_length = np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            edge_lengths.append(edge_length)
        return edge_lengths

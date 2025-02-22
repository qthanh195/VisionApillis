import cv2
import math
import numpy as np
import time

from utils.config import thresh_bg, thresh_pp, ratio
   
class ImageProcess:

    def pre_processing(self, image):
        if len(image.shape) == 2:
            image_gray = image 
        else:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        output_image = None
        # center_crop = None
        img = cv2.blur(image_gray, (5, 5), 2)
        img = img[2100:,]
        # cv2.imwrite("aaa.jpg", img)
        ret, thresh1 = cv2.threshold(img, thresh_bg, 255, cv2.THRESH_BINARY)
        thresh1 = cv2.blur(thresh1, (3, 3), 2)
        #tim 2 duong tron
        circles = cv2.HoughCircles(thresh1, cv2.HOUGH_GRADIENT, dp=1.2,  minDist=1000,param1=50,param2=30,minRadius=40, maxRadius=50 )
        
        x1,y1,r1 = circles[0][0]
        p1 = (int(x1), int(y1)+2100)
        x2,y2,r2 = circles[0][1]
        p2 = (int(x2), int(y2)+2100)
        
        angle = self.calculate_angle(p1, p2)
        #Xoay anh
        rotated_image,matrix_rotate = self.rotate_image(image, 180 + angle) 
        cv2.imwrite("new_img_2102.jpg", rotated_image)
        center_crop_befor = (abs(p1[0] - p2[0])//2+min(p1[0],p2[0]), abs(p1[1] - p2[1])//2+min(p1[1],p2[1]))
        center_crop_after = self.transform_point(center_crop_befor, matrix_rotate)
        # cv2.circle(rotated_image, center_crop_after, 20, (0, 0, 255), -1)
        
        
        output_image= rotated_image[center_crop_after[1]-100:center_crop_after[1]+2000, center_crop_after[0]-1750:center_crop_after[0]+1750]
        # cv2.imwrite("image_output.jpg", output_image)
        
        if len(image.shape) == 2:
            new_img = np.full((output_image.shape[0]+10, output_image.shape[1]), 255, dtype=np.uint8)
            
            new_img[:output_image.shape[0], :] = output_image
            new_img_gray = new_img
            return new_img, new_img_gray
        else:
            new_img = np.full((output_image.shape[0]+10, output_image.shape[1],3), 255, dtype=np.uint8)
            new_img[:output_image.shape[0], :] = output_image
            new_img_gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
            return new_img, new_img_gray
            
    def calculate_angle(self,p1, p2):
        if p1[0] > p2[0]:
            p1, p2 = p2, p1
        delta_x = p2[0] - p1[0]
        delta_y = p2[1] - p1[1]

        # Tính góc
        angle_rad = math.atan2(delta_y, delta_x)
        angle_deg = math.degrees(angle_rad)

        # print("angle", angle_deg)

        return angle_deg
    
    def rotate_image(self, image, angle):
        (h, w) = image.shape[:2] 
        center = (w // 2, h // 2) 
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h)) 
        return rotated_image, rotation_matrix
    
    def transform_point(self, p, rotation_matrix):
        new_x = rotation_matrix[0, 0] * p[0] + rotation_matrix[0, 1] * p[1] + rotation_matrix[0, 2]
        new_y = rotation_matrix[1, 0] * p[0] + rotation_matrix[1, 1] * p[1] + rotation_matrix[1, 2]
        new_point = (int(new_x), int(new_y))
        return new_point

    def remove_contour(self,new_img_gray, threshold_value, area_min, area_max):
        img = cv2.blur(new_img_gray, (5, 5), 2)
        _, thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
        thresh = cv2.blur(thresh, (3, 3), 2)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            # print(area)
            if area_min < area < area_max:
                return cnt
        print("no contour")
        return None

    def draw_dimension(self,image, point1, point2):
        # Tính khoảng cách Euclidean giữa 2 điểm
        # self.get_distance(point1, point2)
        distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
        distance_mm = distance * self.ratio
        
        print(distance_mm)
        # distance_text = f"{distance_mm:.2f} mm ({distance:.2f} px)"
        # distance_text = f"{distance:.0f} px"
        distance_text = f"{distance_mm:.2f} mm"
        

        # Vẽ đường thẳng nối 2 điểm
        cv2.line(image, point1, point2, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

        # Vẽ mũi tên hai đầu (nếu cần)
        cv2.arrowedLine(image, point1, point2, color=(255, 0, 0), thickness=2, tipLength=0.3)
        cv2.arrowedLine(image, point2, point1, color=(255, 0, 0), thickness=2, tipLength=0.3)

        # Tính vị trí đặt văn bản (ở giữa đoạn thẳng)
        mid_point = (((point1[0] + point2[0]) // 2)+5, ((point1[1] + point2[1]) // 2)-8)
        # Hiển thị giá trị khoảng cách
        cv2.putText(image, distance_text, mid_point, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
        
    def find_extreme_point(self, contour, axis, extreme_type, value):
        """
        Tìm điểm cực trị trong contour trên trục chỉ định (x hoặc y).
        Parameters:
        - contour: danh sách điểm (numpy array)
        - axis: "x" hoặc "y" (chỉ định trục để tìm cực trị)
        - extreme_type: "max" hoặc "min" (chỉ định cực trị lớn nhất hoặc nhỏ nhất)
        - value: giá trị cố định của trục còn lại (vd: x hoặc y)

        Returns:
        - Điểm cực trị (tuple) hoặc None nếu không tìm thấy.
        """
        if axis == "x":
            # Tìm tất cả các điểm trên contour với x = value
            points = [point[0] for point in contour if point[0][0] == value]
            
            if not points:
                return None
            # Trả về điểm có y lớn nhất hoặc nhỏ nhất
            if extreme_type == "max":
                return max(points, key=lambda p: p[1])
            elif extreme_type == "min":
                return min(points, key=lambda p: p[1])
        elif axis == "y":
            # Tìm tất cả các điểm trên contour với y = value
            points = [point[0] for point in contour if point[0][1] == value]
            # print(points)
            if not points:
                return None
            # Trả về điểm có x lớn nhất hoặc nhỏ nhất
            if extreme_type == "max":
                return max(points, key=lambda p: p[0])
            elif extreme_type == "min":
                return min(points, key=lambda p: p[0])
        return None

    def get_dimension(self, image):
        new_img, new_img_gray = self.pre_processing(image)
        (h, w) = new_img.shape[:2]
        center = (w // 2, h // 2) 
        x1 = center[0] - 800
        x2 = center[0] + 800
        y1 = center[1] - 600
        y2 = center[1] + 700
        cnt1 = self.remove_contour(new_img_gray, thresh_bg, 6000000, 7200000) # tách nền
        cnt2 = self.remove_contour(new_img_gray, thresh_pp, 5500000, 7200000) # Tách giấy và kim loại
        
        # cv2.line(new_img, (x1, 0), (x1, h), color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        # cv2.line(new_img, (x2, 0), (x2, h), color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        # cv2.line(new_img, (0, y1), (w, y1), color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        # cv2.line(new_img, (0, y2), (w, y2), color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        # cv2.drawContours(new_img, [cnt1], -1, (0, 255, 0), -1)
        # cv2.drawContours(new_img, [cnt2], -1, (0, 255, 0), -1)
        
        
        
        
        if cnt1 is not None and cnt2 is not None:
            # cv2.imwrite("./Image/test222.jpg", self.new_img)
            # time.sleep(1)
            # pos 1
            p1_1 = self.find_extreme_point(cnt1, axis="x", extreme_type="min", value=x2)
            p1_2 = self.find_extreme_point(cnt2, axis="x", extreme_type="min", value=x2)
            p1 = self.distance_tow_point(p1_1, p1_2)
            # self.draw_dimension(self.new_img, p1_1, p1_2)
            
            # pos 2
            p2_1 = self.find_extreme_point(cnt1, axis="x", extreme_type="min", value=x1)
            p2_2 = self.find_extreme_point(cnt2, axis="x", extreme_type="min", value=x1)
            p2 = self.distance_tow_point(p2_1, p2_2)
            # self.draw_dimension(self.new_img, p2_1, p2_2)
            # time.sleep(1)

            # pos 3
            p3_1 = self.find_extreme_point(cnt1, axis="y", extreme_type="max", value=y2)
            p3_2 = self.find_extreme_point(cnt2, axis="y", extreme_type="max", value=y2)
            p3 = self.distance_tow_point(p3_1, p3_2)
            # self.draw_dimension(self.new_img, p3_1, p3_2)

            # pos 4
            p4_1 = self.find_extreme_point(cnt1, axis="y", extreme_type="max", value=y1)
            p4_2 = self.find_extreme_point(cnt2, axis="y", extreme_type="max", value=y1)
            p4 = self.distance_tow_point(p4_1, p4_2)
            # self.draw_dimension(self.new_img, p4_1, p4_2)

            # pos 5
            p5_1 = self.find_extreme_point(cnt1, axis="y", extreme_type="min", value=y2)
            p5_2 = self.find_extreme_point(cnt2, axis="y", extreme_type="min", value=y2)
            p5 = self.distance_tow_point(p5_1, p5_2)
            # self.draw_dimension(self.new_img, p5_1, p5_2)

            # pos 6
            p6_1 = self.find_extreme_point(cnt1, axis="y", extreme_type="min", value=y1)
            p6_2 = self.find_extreme_point(cnt2, axis="y", extreme_type="min", value=y1)
            p6 = self.distance_tow_point(p6_1, p6_2)
            # self.draw_dimension(self.new_img, p6_1, p6_2)
            print("Done")
            # cv2.imwrite("showcheck.jpg", self.new_img)
            
            return new_img, p1, p2, p3, p4, p5, p6

    def distance_tow_point(self, p1, p2):
        """
        Tính khoảng cách giữa hai điểm.
        """
        # print("ratio", (np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)))
        
        return (np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)) * ratio
    
    def detect_object(self, image):
        image_org = image[2100:,]

        if len(image_org.shape) == 2:
            img = cv2.blur(image_org, (5, 5), 2)
        else:
            img = cv2.blur(cv2.cvtColor(image_org, cv2.COLOR_BGR2GRAY), (5, 5), 2)
        ret, thresh1 = cv2.threshold(img, thresh_bg, 255, cv2.THRESH_BINARY)
        thresh1 = cv2.blur(thresh1, (3, 3), 2)

        #tim 2 duong tron
        circles = cv2.HoughCircles(thresh1, cv2.HOUGH_GRADIENT, dp=1.2,  minDist=1000,param1=50,param2=30,minRadius=40, maxRadius=50 )
        if circles is None or len(circles[0]) < 2 or len(circles[0])>2:
            return False
        x1,y1,r1 = circles[0][0]
        p1 = (int(x1), int(y1)+2100)
        x2,y2,r2 = circles[0][1]
        p2 = (int(x2), int(y2)+2100)
        # print("p1", p1)
        # print("p2", p2)
        if max(p1[0], p2[0]) > 3200 or min(p1[0], p2[0]) < 650 or max(p1[1], p2[1]) > 2440 or min(p1[1], p2[1]) < 2200:
            return False
        agl = self.calculate_angle(p1, p2)
        if  agl < -3 or agl > 3:
            return False
        return True

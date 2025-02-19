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
        center_crop = None
        img = cv2.blur(image_gray, (5, 5), 2)
        img = img[2100:,]
        # cv2.imwrite("aaa.jpg", img)
        ret, thresh1 = cv2.threshold(img, thresh_bg, 255, cv2.THRESH_BINARY)
        thresh1 = cv2.blur(thresh1, (3, 3), 2)
        #tim 2 duong tron
        circles = cv2.HoughCircles(thresh1, cv2.HOUGH_GRADIENT, dp=1.2,  minDist=1000,param1=50,param2=30,minRadius=40, maxRadius=50 )
        
        x1,y1,r1 = circles[0][0]
        p1 = (int(x1), int(y1)+2100)
        # p1 = (int(x1), int(y1))
        x2,y2,r2 = circles[0][1]
        p2 = (int(x2), int(y2)+2100)
        # p2 = (int(x2), int(y2))
        angle = self.calculate_angle(p1, p2)
        # print(p1)
        if angle > 0:
            angle = angle
        #Xoay anh
        rotated_image = self.rotate_image(image, angle) 
        center_crop = (abs(p1[0] - p2[0])//2+min(p1[0],p2[0]), abs(p1[1] - p2[1])//2+min(p1[1],p2[1]))
        
        output_image= rotated_image[center_crop[1]-2000:center_crop[1]+100, center_crop[0]-1600:center_crop[0]+1600]
        if len(image.shape) == 2:
            new_img = np.full((output_image.shape[0]+10, output_image.shape[1]), 255, dtype=np.uint8)
            

            new_img[10:, :] = output_image
            new_img_gray = new_img
            return new_img, new_img_gray
        else:
            new_img = np.full((output_image.shape[0]+10, output_image.shape[1],3), 255, dtype=np.uint8)
            new_img[10:, :] = output_image
            new_img_gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
            return new_img, new_img_gray
            
    def calculate_angle(self, p1, p2):
        delta_x = p2[0] - p1[0]
        delta_y = p2[1] - p1[1]
        angle_rad = math.atan2(delta_y, delta_x) 
        angle_deg = math.degrees(angle_rad)    
        return angle_deg
    
    def rotate_image(self, image, angle):
        (h, w) = image.shape[:2] 
        center = (w // 2, h // 2) 
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h)) 
        return rotated_image

    def remove_contour(self,new_img_gray, threshold_value, area_min, area_max):
        img = cv2.blur(new_img_gray, (5, 5), 2)
        _, thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
        thresh = cv2.blur(thresh, (3, 3), 2)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cv2.imwrite("./thresh.jpg", thresh)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            print("dien tich ",area)
            if area_min < area < area_max:
                # cv2.drawContours(self.new_img, [cnt], -1, (0, 255, 0), 2)
                return cnt
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
        
        cnt1 = self.remove_contour(new_img_gray, thresh_bg, 5436181.0, 6000000) # tách nền
        cnt2 = self.remove_contour(new_img_gray, thresh_pp, 5091726.5, 6000000) # Tách giấy và kim loại

        if cnt1 is not None and cnt2 is not None:
            # cv2.imwrite("./Image/test222.jpg", self.new_img)
            # time.sleep(1)
            # pos 1
            p1_1 = self.find_extreme_point(cnt1, axis="x", extreme_type="max", value=x1)
            p1_2 = self.find_extreme_point(cnt2, axis="x", extreme_type="max", value=x1)
            p1 = self.distance_tow_point(p1_1, p1_2)
            # self.draw_dimension(self.new_img, p1_1, p1_2)
            
            # pos 2
            p2_1 = self.find_extreme_point(cnt1, axis="x", extreme_type="max", value=x2)
            p2_2 = self.find_extreme_point(cnt2, axis="x", extreme_type="max", value=x2)
            p2 = self.distance_tow_point(p2_1, p2_2)
            # self.draw_dimension(self.new_img, p2_1, p2_2)
            # time.sleep(1)

            # pos 3
            p3_1 = self.find_extreme_point(cnt1, axis="y", extreme_type="min", value=y1)
            p3_2 = self.find_extreme_point(cnt2, axis="y", extreme_type="min", value=y1)
            p3 = self.distance_tow_point(p3_1, p3_2)
            # self.draw_dimension(self.new_img, p3_1, p3_2)

            # pos 4
            p4_1 = self.find_extreme_point(cnt1, axis="y", extreme_type="min", value=y2)
            p4_2 = self.find_extreme_point(cnt2, axis="y", extreme_type="min", value=y2)
            p4 = self.distance_tow_point(p4_1, p4_2)
            # self.draw_dimension(self.new_img, p4_1, p4_2)

            # pos 5
            p5_1 = self.find_extreme_point(cnt1, axis="y", extreme_type="max", value=y1)
            p5_2 = self.find_extreme_point(cnt2, axis="y", extreme_type="max", value=y1)
            p5 = self.distance_tow_point(p5_1, p5_2)
            # self.draw_dimension(self.new_img, p5_1, p5_2)

            # pos 6
            p6_1 = self.find_extreme_point(cnt1, axis="y", extreme_type="max", value=y2)
            p6_2 = self.find_extreme_point(cnt2, axis="y", extreme_type="max", value=y2)
            p6 = self.distance_tow_point(p6_1, p6_2)
            # self.draw_dimension(self.new_img, p6_1, p6_2)
            print("Done")
            # cv2.imwrite("showcheck.jpg", self.new_img)
            
            return new_img, p1, p2, p3, p4, p5, p6

    def distance_tow_point(self, p1, p2):
        """
        Tính khoảng cách giữa hai điểm.
        """
        return (np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)) * ratio
    

def detect(image_org, thresh_bg,  thresh_pp):
    image_org = image_org[2100:,]
    # cv2.imwrite("./aaa.jpg", image_org)
    # cv2.imshow("image", image_org)
    # cv2.waitKey(0)
    if len(image_org.shape) == 2:
        img = cv2.blur(image_org, (5, 5), 2)
    else:
        img = cv2.blur(cv2.cvtColor(image_org, cv2.COLOR_BGR2GRAY), (5, 5), 2)
    ret, thresh1 = cv2.threshold(img, thresh_bg, 255, cv2.THRESH_BINARY)
    # Applies a Gaussian blur to the `thresh1` image to smooth out noise and small details. This can help improve the performance of subsequent image processing operations.
    
    # The blur is applied with a 3x3 kernel and a standard deviation of 2 in both the x and y directions.
    thresh1 = cv2.blur(thresh1, (3, 3), 2)
    #tim 2 duong tron
    circles = cv2.HoughCircles(thresh1, cv2.HOUGH_GRADIENT, dp=1.2,  minDist=1000,param1=50,param2=30,minRadius=40, maxRadius=50 )
    # print(len(circles[0]))
    # if circles is None:
    #     print("aaaa")
    if circles is None or len(circles[0]) < 2 or len(circles[0])>2:
        return False
    return True

def handle_stream(video,thresh_bg, thresh_pp):
    circles = False
    new_img = None
    flag = False
    mask = np.full((2110, 3200,3), 255, dtype=np.uint8)
    while True:
        # stat_time = time.time()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ret, image = video.read()
        if not ret:
            print("Không thể đọc thêm frame hoặc video đã kết thúc.")
            break
        img = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)
        cv2.imshow("Video", img)
        
        if new_img is not None:
            cv2.imshow("new_img", new_img)

        circles = detect(image, thresh_bg, thresh_pp)
        if not circles:
            flag = False
            continue
        if circles and not flag:
            print("Có vật")
            img_process = ImageProcess(image, thresh_bg, thresh_pp)
            new_img = img_process.dimension()
            flag = True
            new_img = cv2.resize(new_img, (0, 0), fx=0.4, fy=0.4)
        
    video.release()
    cv2.destroyAllWindows()
    
def handle_stream_with_flag(video,thresh_bg, thresh_pp):
    circles = False
    new_img = None
    flag = False
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key  == ord('q'):
            break
        
        ret, image = video.read()
        if not ret:
            print("Không thể đọc thêm frame hoặc video đã kết thúc.")
            break
        img = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)
        cv2.imshow("Video", img)
        if key == ord('s'):
            print("Có vật")
            img_process = ImageProcess(image, thresh_bg, thresh_pp)
              
    video.release()
    cv2.destroyAllWindows()
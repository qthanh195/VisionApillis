# Vision Project

## Mô tả
Dự án này sử dụng camera Basler để chụp và xử lý hình ảnh.

## Yêu cầu
- Python 3.x
- Các thư viện được liệt kê trong `requirements.txt`

## Cài đặt
1. Cài đặt Python 3.x
2. Cài đặt các thư viện được liệt kê trong `requirements.txt` bằng lệnh: pip install -r requirements.txt

 Chạy file chính: 
python ApillisApp.py


## Cân chỉnh camera

- Định dang ảnh: Mono8
- Độ tìm độ phơi sáng phù hợp ExposureAuto giúp camera tự động điều chỉnh thời gian phơi sáng để đảm bảo rằng hình ảnh không quá sáng hoặc quá tối.
- BalanceWhiteAuto giúp camera tự động điều chỉnh cân bằng trắng để đảm bảo rằng màu sắc của hình ảnh là chính xác và không bị ám màu. Điều này rất quan trọng khi điều kiện ánh sáng có nhiệt độ màu khác nhau, chẳng hạn như ánh sáng tự nhiên và ánh sáng nhân tạo. Giúp các vùng trắng trong ảnh thật sự là trắng chứ không phải xám hay màu khác, tăng độ tương phản của vật.

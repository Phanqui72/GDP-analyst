# 📈 Báo cáo Dự báo Kinh tế & Kịch bản Tăng trưởng 2030

## 1. Thông tin chung (Input)
- **Dữ liệu GDP:** Chuỗi thời gian GDP tổng số (1995-2024) từ `data/processed/gdp_sectors_processed.csv`.
- **Dữ liệu Tỷ giá:** Tỷ giá USD/VND lịch sử để chuyển đổi sang giá trị USD.
- **Chỉ số TFP:** Tỷ lệ đóng góp của TFP vào tăng trưởng (2011-2023) để đánh giá chất lượng tăng trưởng trong các kịch bản.

## 2. Yêu cầu thực hiện (Requirements)
- Huấn luyện mô hình **ARIMA** (tuyến tính) và **LSTM** (phi tuyến) để dự báo GDP đến năm 2030.
- Xây dựng 3 kịch bản:
    - **Cơ sở (Base):** Theo xu hướng dự báo của mô hình.
    - **Lạc quan (Optimistic):** Tăng trưởng cao nhờ đột phá công nghệ và TFP (>45%).
    - **Bi quan (Pessimistic):** Chịu ảnh hưởng bởi các cú sốc ngoại biên hoặc suy thoái ngành công nghiệp.
- Đánh giá khả năng vượt bẫy thu nhập trung bình (Middle-income trap) dựa trên ngưỡng thu nhập cao của World Bank.

## 3. Quy trình thực hiện (Process)
1. **Tiền xử lý:** Chuẩn hóa chuỗi thời gian, chuyển đổi GDP sang USD.
2. **Mô hình hóa ARIMA:** Tìm thông số (p,d,q) tối ưu, đánh giá sai số (RMSE, MAE).
3. **Mô hình hóa LSTM:** Xây dựng mạng neural hồi quy, training với dữ liệu chuẩn hóa.
4. **Hợp nhất dự báo:** Kết hợp kết quả từ 2 mô hình (Ensemble) để tăng độ chính xác.
5. **Xây dựng kịch bản:** Điều chỉnh tốc độ tăng trưởng giả định dựa trên biến số TFP và bối cảnh vĩ mô.
6. **Phân tích bẫy thu nhập:** So sánh GDP bình quân đầu người dự báo với các mốc phân loại của World Bank.

## 4. Kết quả đầu ra (Output)
- File Notebook: `notebooks/GDP_Forecasting_2030.ipynb`.
- Biểu đồ dự báo các kịch bản tăng trưởng đến năm 2030.
- Bảng so sánh các mốc thời gian đạt ngưỡng thu nhập theo từng kịch bản.

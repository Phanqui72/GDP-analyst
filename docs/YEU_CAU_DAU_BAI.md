# 📋 YÊU CẦU ĐẦU BÀI CHI TIẾT (ANALYSIS REQUIREMENTS) - CẬP NHẬT V2

## 1. Tầm nhìn & Ý nghĩa bài toán
Xác định con đường phát triển bền vững của Việt Nam thông qua việc bóc tách chất lượng tăng trưởng. Mục tiêu tối thượng là đánh giá khả năng **thoát bẫy thu nhập trung bình** dựa trên hiệu quả sử dụng nguồn lực (TFP) thay vì tích lũy vốn vật chất.

## 2. Các yêu cầu phân tích trọng tâm (Tổng hợp từ Báo cáo Overview & Tài liệu TS. Nguyễn Thị Hương)

### 2.1. Phân tích Động lực Tăng trưởng (Growth Drivers)
- **Tiêu dùng & Đầu tư:** Tương quan giữa chi tiêu tiêu dùng (`NE.CON.TOTL.ZS`) và tích lũy vốn (`NE.GDI.FTOT.ZS`) để xác định nền kinh tế đang dựa vào nội lực tiêu dùng hay thâm dụng đầu tư hạ tầng.
- **Ngoại thương:** Đánh giá độ mở kinh tế qua tỷ trọng Xuất nhập khẩu.

### 2.2. Phân tích Ảnh hưởng & Tương tác của 3 Khu vực Kinh tế
- **Khu vực I (Nông nghiệp):** Đánh giá vai trò "bệ đỡ" giúp ổn định xã hội và kinh tế trong các giai đoạn biến động (Outliers).
- **Khu vực II (Công nghiệp):** Đóng vai trò là "động cơ tăng trưởng". Cần phân tích sự dịch chuyển từ gia công sang chế biến chế tạo có hàm lượng công nghệ cao.
- **Khu vực III (Dịch vụ - Trọng điểm mới):** 
    - Tập trung vào **Logistics, Tài chính và Du lịch**. 
    - Đây là khu vực được kỳ vọng có TFP bùng nổ nhờ chuyển đổi số.
    - Đánh giá vai trò của Dịch vụ trong việc thúc đẩy GNI bình quân đầu người để thoát bẫy thu nhập trung bình.

### 2.3. Chỉ số TFP & Năng suất Lao động (Biến số Chất)
- **TFP:** Là biến số giải thích cốt lõi cho sự tăng trưởng của các khu vực.
- **Năng suất lao động (`SL.GDP.PCAP.EM.KD`):** Sử dụng làm chỉ số bổ trợ cực kỳ quan trọng khi dữ liệu TFP bị thiếu hụt hoặc cần kiểm chứng chéo.

### 2.4. Đối chiếu GDP, GNI & PPP
- Sử dụng **GNI per capita, PPP (`NY.GNP.PCAP.PP.CD`)** để so sánh chính xác mức sống và vị thế của Việt Nam với các đối thủ trong khu vực (Thái Lan, Indonesia, Philippines).
- Phân tích sự chênh lệch giữa GDP và GNI để đánh giá mức độ đóng góp của nội lực kinh tế so với khu vực FDI.

---

## 3. Các mốc kiểm định & Thuật toán
- **Kiểm định:** t-test, ADF, Chi-square.
- **Chẩn đoán điểm gãy:** Sử dụng thuật toán khách quan (Z-score, Isolation Forest) để tìm điểm rơi kinh tế, sau đó đối chiếu với các sự kiện vĩ mô (WTO, khủng hoảng 2008, đại dịch...).
- **Dự báo:** ARIMA và LSTM cho tầm nhìn 2030.

## 4. Tài liệu tham khảo tích hợp
- World Bank Open Data.
- Tổng cục Thống kê (NSO) - Báo cáo 9 tháng năm 2024.
- Chuyên đề TS. Nguyễn Thị Hương (2025) về xu hướng chuyển dịch cơ cấu từ 1986.

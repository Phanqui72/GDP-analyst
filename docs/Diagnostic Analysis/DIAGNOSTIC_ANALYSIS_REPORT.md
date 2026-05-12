# 📊 Báo cáo Chẩn đoán Biến động GDP Việt Nam (Diagnostic Analysis Report)

## 1. Yêu cầu thực hiện (Requirements)
- **Phát hiện (Detection):** Sử dụng các thuật toán Z-score và Isolation Forest để xác định các năm có biến động GDP lệch chuẩn (Outliers).
- **Chẩn đoán (Diagnosis):** Bóc tách nguyên nhân từ 3 khu vực kinh tế (Nông nghiệp, Công nghiệp, Dịch vụ). Đánh giá khu vực nào (II hay III) dẫn đầu sự sụt giảm tại các điểm gãy.
- **Đối chiếu ngoại biên (External Context):** Liên kết các điểm gãy với biến động tỷ giá USD/VND và bối cảnh quốc tế.

## 2. Dữ liệu đầu vào (Input)
- `gdp_sectors_processed.csv`: Dữ liệu GDP bóc tách theo 3 khu vực (1986 - 2024).
- `Dữ liệu Lịch sử USD_VND 1994-2025.csv`: Dữ liệu tỷ giá hối đoái thực tế.
- Báo cáo Overview 7/5: Bối cảnh sự kiện vĩ mô.

## 3. Quá trình thực hiện (Process)
1.  **Tính toán tỷ lệ tăng trưởng (Growth Rate):** Chuyển đổi dữ liệu tuyệt đối sang tỷ lệ % thay đổi hàng năm để loại bỏ yếu tố quy mô.
2.  **Áp dụng thuật toán phát hiện:**
    - **Z-score:** Tìm các năm có độ lệch chuẩn > 1.5 so với trung bình tăng trưởng.
    - **Isolation Forest:** Sử dụng mô hình học máy để cô lập các điểm dữ liệu bất thường trong không gian đa chiều.
3.  **Phân tích bóc tách (Decomposition):** Tại mỗi năm "outlier", so sánh tốc độ tăng trưởng của Khu vực II (Công nghiệp) và Khu vực III (Dịch vụ) để xác định "động cơ" hoặc "điểm nghẽn".
4.  **Tích hợp dữ liệu tỷ giá:** Tính toán trung bình năm của tỷ giá USD/VND và tính % thay đổi để đối chiếu với các cú sốc tăng trưởng.

## 4. Kết quả đầu ra (Output)

### 4.1. Các điểm gãy phát hiện được (Detected Breakpoints)
Dựa trên phân tích Z-score và Isolation Forest, các giai đoạn sau được xác định là điểm gãy quan trọng:

| Giai đoạn | Loại biến động | Nguyên nhân dẫn đầu | Tác động Tỷ giá (FX) |
| :--- | :--- | :--- | :--- |
| **1998 - 1999** | Sụt giảm (Drop) | **Khu vực III (Dịch vụ)** | Devaluation mạnh (~10-15%) |
| **2008 - 2009** | Sụt giảm (Drop) | **Khu vực II (Công nghiệp)** | Biến động mạnh (Khủng hoảng tài chính) |
| **2020 - 2021** | Sụt giảm (Drop) | **Khu vực III (Dịch vụ)** | Ổn định tương đối (SBV can thiệp) |
| **2010** | Tăng đột biến* | **Hồi phục đa ngành** | Điều chỉnh tỷ giá mạnh (+7.3%) |

*\*Lưu ý: Năm 2010 có sự tăng trưởng danh nghĩa đột biến do thay đổi năm gốc và lạm phát cao.*

### 4.2. Chẩn đoán chi tiết (Diagnosis)
- **Khủng hoảng 1998 (Á vận hội/Khủng hoảng Châu Á):** Khu vực III sụt giảm mạnh nhất do du lịch và dòng vốn FDI vào dịch vụ bị ngưng trệ.
- **Khủng hoảng 2008 (Toàn cầu):** Khu vực II dẫn đầu sự sụt giảm. Công nghiệp chế biến chế tạo hướng về xuất khẩu bị ảnh hưởng trực tiếp bởi sự suy sụp của cầu thế giới. Tỷ giá USD/VND tăng mạnh gây áp lực lên chi phí nhập khẩu nguyên liệu.
- **Đại dịch 2020 (COVID-19):** Một trường hợp đặc biệt khi Khu vực III (Dịch vụ) chịu đòn giáng nặng nề nhất do các lệnh phong tỏa, trong khi Khu vực II vẫn duy trì được đà tăng trưởng nhờ xuất khẩu thiết bị điện tử.

### 4.3. Đối chiếu ngoại biên & Tỷ giá
- Các điểm gãy GDP luôn đi kèm với sự điều chỉnh tỷ giá của Ngân hàng Nhà nước để duy trì lợi thế xuất khẩu.
- Giai đoạn 2008-2011 chứng kiến sự mất giá của VND liên tục, phản ánh áp lực từ thâm hụt thương mại và lạm phát, trùng khớp với giai đoạn tăng trưởng công nghiệp bất ổn.

## 5. Kết luận của Chuyên gia
Sự dịch chuyển cơ cấu từ Công nghiệp (II) sang Dịch vụ (III) đang diễn ra nhưng tính dễ tổn thương của Dịch vụ trước các cú sốc phi kinh tế (như dịch bệnh) là rất cao. Để thoát bẫy thu nhập trung bình, Việt Nam cần củng cố Khu vực II bằng các ngành công nghệ cao để làm "bệ đỡ" cho Khu vực III phát triển bền vững.

---
*Tài liệu được phê duyệt bởi Chuyên gia Phân tích Dữ liệu Cao cấp.*

# 📊 TÀI LIỆU PHÂN TÍCH KHÁM PHÁ DỮ LIỆU (EXPLORATORY DATA ANALYSIS - EDA)

## 1. Tổng quan
Tài liệu này mô tả chi tiết quy trình, phương pháp và các kết quả đạt được trong giai đoạn phân tích khám phá (EDA) của dự án Phân tích Kinh tế Vĩ mô Việt Nam. Mục tiêu chính là chuyển đổi các con số khô khan từ dữ liệu thô thành các thông tin trực quan có giá trị (insights).

---

## 2. Dữ liệu đầu vào (Input Data)
EDA sử dụng các tập dữ liệu đã qua tiền xử lý (Preprocessing) nằm trong thư mục `data/processed/`:

- **`gdp_sectors_processed.csv`**: Chứa giá trị GDP phân theo 3 khu vực kinh tế (Nông nghiệp, Công nghiệp, Dịch vụ) từ năm 1986 - 2024.
- **`gdp_usage_processed.csv`**: Chứa các thành phần sử dụng GDP (Tiêu dùng cuối cùng, Tích lũy tài sản, Xuất nhập khẩu ròng) từ năm 1995 - 2024.
- **`tfp_contribution_processed.csv`**: Chứa số liệu về đóng góp của các nhân tố Vốn, Lao động và TFP vào tăng trưởng GDP.

---

## 3. Yêu cầu thực hiện (Requirements)
Dựa trên yêu cầu từ chuyên gia, giai đoạn này cần đạt được các mục tiêu sau:
- **Tính toàn diện:** Trực quan hóa từng dataset một cách chi tiết để tìm ra các đặc trưng (features) và xu hướng.
- **Tính chiều sâu:** Trích xuất được các insight về:
    - Sự chuyển dịch cơ cấu ngành kinh tế qua các thời kỳ.
    - Động lực chính thúc đẩy GDP (Tiêu dùng hay Đầu tư?).
    - Chất lượng tăng trưởng (Tăng trưởng dựa trên thâm dụng vốn hay hiệu quả kỹ thuật TFP?).
- **Tính trực quan (Executive View):** Xây dựng một **Master Dashboard** tổng hợp, giúp người xem nắm bắt toàn bộ bức tranh kinh tế trong "một cái nhìn" (One-look) mà không cần giải thích thêm.

---

## 4. Cách thức thực hiện (Methodology)

### Bước 1: Thiết lập môi trường & Cấu hình trực quan
- Sử dụng thư viện `matplotlib` và `seaborn` để tạo các biểu đồ tĩnh chất lượng cao.
- Cấu hình style `whitegrid` và font chữ hỗ trợ tiếng Việt để đảm bảo tính chuyên nghiệp.
- Thiết lập thang đo Logarithmic (Log scale) cho các biểu đồ có giá trị tăng trưởng đột biến qua nhiều thập kỷ.

### Bước 2: Phân tích Chuyển dịch Cơ cấu (Structural Shift)
- **Kỹ thuật:** Sử dụng biểu đồ chồng (Stacked Area Chart).
- **Mục đích:** Làm nổi bật sự thay đổi tỷ trọng giữa 3 khu vực kinh tế. Cho thấy quá trình chuyển đổi từ một nền kinh tế nông nghiệp sang công nghiệp và dịch vụ.

### Bước 3: Phân tích Động lực Tăng trưởng (GDP Usage)
- **Kỹ thuật:** Biểu đồ đường (Line Chart) kết hợp thang Log.
- **Mục đích:** So sánh tốc độ phát triển của Tiêu dùng, Đầu tư và Xuất khẩu ròng. Xác định xem nền kinh tế đang vận hành dựa trên nội lực tiêu dùng hay dựa trên thu hút đầu tư.

### Bước 4: Phân tích Chất lượng Tăng trưởng (TFP)
- **Kỹ thuật:** Biểu đồ cột chồng (Stacked Bar Chart).
- **Mục đích:** Bóc tách phần trăm đóng góp của Vốn (Capital), Lao động (Labor) và TFP (Total Factor Productivity). Đây là chỉ số quan trọng để đánh giá mức độ hiện đại hóa của nền kinh tế.

### Bước 5: Tích hợp Master Dashboard
- Sử dụng `gridspec` của Matplotlib để phân chia bố cục màn hình (2x2).
- Kết hợp 4 biểu đồ quan trọng nhất vào một khung hình duy nhất.
- Tinh chỉnh màu sắc đồng nhất (Color branding) và thêm tiêu đề tổng hợp (Suptitle) để tạo ra bản báo cáo trực quan cấp cao (Executive Report).

---

## 5. Kết quả đầu ra (Output)
- **Notebook chính:** `notebooks/FINAL_EXECUTIVE_DASHBOARD.ipynb`
- **Dashboard:** Một bảng điều khiển tổng thể gồm 4 phân khu:
    1. Quy mô GDP (Area Chart).
    2. Cơ cấu ngành (Stacked Area %).
    3. Cân bằng Tiêu dùng - Đầu tư (Grouped Bar).
    4. Đóng góp TFP (Stacked Bar %).

---
> **Lưu ý:** Kết quả từ giai đoạn EDA này sẽ là tiền đề cho các phép kiểm định thống kê và mô hình dự báo trong các giai đoạn tiếp theo.

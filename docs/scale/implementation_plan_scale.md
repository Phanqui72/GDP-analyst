# 🚀 Kế hoạch Mở rộng Phân tích Chẩn đoán (Scale Implementation Plan)

## 1. Tầm nhìn
Mục tiêu của tài liệu này là cung cấp lộ trình chi tiết để **chứng minh và giải thích sâu** các kết luận về điểm gãy kinh tế. Hiện tại, dữ liệu ở mức độ gộp (Aggregate) 3 khu vực chưa đủ để bóc tách các nguyên nhân "vi mô" (như du lịch, logistics hay xuất khẩu điện tử).

## 2. Các nhóm dữ liệu cần thu thập bổ sung (Data Collection)

### 2.1. Nhóm Dữ liệu Thứ cấp (Sub-sector Data)
- **Khu vực III (Dịch vụ):** Cần bóc tách ít nhất 5 ngành trọng yếu:
    - Lưu trú và ăn uống (Du lịch).
    - Vận tải kho bãi (Logistics).
    - Tài chính, ngân hàng và bảo hiểm.
    - Hoạt động kinh doanh bất động sản.
    - Bán buôn và bán lẻ.
- **Khu vực II (Công nghiệp):** Bóc tách:
    - Công nghiệp chế biến, chế tạo (Manufacturing) - Đặc biệt là ngành Điện tử và Dệt may.
    - Xây dựng.
    - Khai khoáng.

### 2.2. Nhóm Dữ liệu Ngoại biên (External Drivers)
- **FDI theo ngành:** Dòng vốn đầu tư trực tiếp nước ngoài vào từng khu vực tại các mốc 2008 và 2020.
- **Cán cân Thương mại chi tiết:** Kim ngạch xuất nhập khẩu theo nhóm hàng (Hàng hóa tiêu dùng vs. Nguyên liệu sản xuất).
- **Chỉ số Giá Tiêu dùng (CPI):** Để tách biệt tăng trưởng thực và tăng trưởng danh nghĩa (đặc biệt cho giai đoạn 2008-2010).

## 3. Lộ trình Chứng minh Logic (Analytical Roadmap)

### Bước 1: Phân tích đóng góp chi tiết (Shift-Share Analysis)
- Sử dụng phương pháp Shift-Share để xác định xem sự sụt giảm là do xu hướng chung của ngành toàn cầu hay do năng suất nội tại của Việt Nam tại thời điểm đó.

### Bước 2: Kiểm định quan hệ nhân quả (Granger Causality)
- Kiểm định xem Biến động Tỷ giá có thực sự "gây ra" sự sụt giảm ở Khu vực II (do chi phí nhập khẩu) hay không.
- Kiểm định quan hệ giữa tăng trưởng Dịch vụ và tiêu dùng hộ gia đình (từ `gdp_usage_processed.csv`).

### Bước 3: Phân tích Phản hồi Xung (Impulse Response)
- Xây dựng mô hình VAR (Vector Autoregression) để xem sau bao nhiêu quý thì một cú sốc tỷ giá hoặc cú sốc ngoại thương tác động tối đa đến GDP.

## 4. Giao nhiệm vụ cho Team thu thập dữ liệu
- **Nhiệm vụ 1:** Truy xuất dữ liệu Niên giám Thống kê (GSO) cho các ngành cấp 2 từ năm 1995 - 2024.
- **Nhiệm vụ 2:** Thu thập báo cáo World Bank về chỉ số LPI (Logistics Performance Index) của Việt Nam qua các năm.
- **Nhiệm vụ 3:** Tổng hợp dữ liệu tỷ giá trung tâm và tỷ giá thị trường tự do tại các thời điểm "phá giá" năm 2008, 2011.

---
*Lập bởi: Chuyên gia Phân tích Dữ liệu - Antigravity AI.*

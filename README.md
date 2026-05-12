# 🇻🇳 Dự án Phân tích Cơ cấu Kinh tế Việt Nam & Chỉ số TFP

## 📋 Giới thiệu
Dự án tập trung vào việc phân tích sự chuyển dịch cơ cấu giữa các khu vực kinh tế (Nông nghiệp, Công nghiệp, Dịch vụ) gắn liền với chỉ số TFP (Total Factor Productivity - Năng suất nhân tố tổng hợp). Mục tiêu là đưa ra các nhận định và dự báo về định hướng phát triển quốc gia, đánh giá khả năng vượt qua bẫy thu nhập trung bình.

## 📁 Cấu trúc Thư mục
- `data/`
    - `raw/`: Chứa các dữ liệu thô từ GSO, World Bank và dữ liệu tỷ giá.
    - `processed/`: Dữ liệu sau khi đã được làm sạch và chuẩn hóa.
- `docs/`: Tài liệu kỹ thuật và yêu cầu bài toán.
    - `DATA_PREPROCESSING.md`: Tài liệu chi tiết về quy trình tiền xử lý dữ liệu.
    - `YEU_CAU_DAU_BAI.md`: Mô tả yêu cầu và mục tiêu phân tích.
    - `IMPLEMENTATION_PLAN.md`: Kế hoạch thực hiện dự án.
- `notebooks/`: Các file Jupyter Notebook cho từng giai đoạn.
    - `Pre_processing.ipynb`: Quy trình làm sạch và chuẩn bị dữ liệu.
- `outputs/`: Các biểu đồ, báo cáo và kết quả mô hình.

## 🛠️ Công nghệ sử dụng
- **Ngôn ngữ:** Python
- **Thư viện chính:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn.
- **Dữ liệu:** GSO, World Bank, Yahoo Finance (Exchange rates).

---
*Dự án đang trong quá trình thực hiện giai đoạn: Audit & Preprocessing.*
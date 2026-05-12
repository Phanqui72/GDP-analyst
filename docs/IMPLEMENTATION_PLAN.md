# 🚀 KẾ HOẠCH THỰC HIỆN DỰ ÁN (IMPLEMENTATION PLAN)

## Giai đoạn 1: Khởi tạo & Audit Dữ liệu (Tuần 1)
- [x] Thiết lập cấu trúc thư mục chuẩn: `data/`, `notebooks/`, `docs/`, `outputs/`.
- [x] Import dữ liệu Master DataFrame từ `data/raw/`.
- [x] Xây dựng **Overview Dashboard**: Biểu đồ "One-Look" tại `FINAL_EXECUTIVE_DASHBOARD.ipynb`.

## Giai đoạn 2: Phân tích Khám phá & Kiểm định (Tuần 2)
- [x] EDA chuyên sâu các đặc trưng chuỗi thời gian.
- [x] Thực hiện kiểm định ADF, Granger Causality.
- [ ] Phân tích tương quan giữa TFP và Năng suất lao động (`SL.GDP.PCAP.EM.KD`).

## Giai đoạn 3: Phát hiện & Chẩn đoán Điểm Gãy (Diagnostic Analysis) (Tuần 3)
- [ ] **Phát hiện:** Dùng Z-score/Isolation Forest để xác định các năm biến động lệch chuẩn.
- [ ] **Chẩn đoán:** Bóc tách nguyên nhân từ 3 khu vực. Đánh giá xem sự sụt giảm ở các điểm gãy có phải do khu vực II (Công nghiệp) hay khu vực III (Dịch vụ) dẫn đầu.
- [ ] **Đối chiếu ngoại biên:** Liên kết các điểm gãy với biến động tỷ giá USD/VND và bối cảnh quốc tế từ báo cáo Overview.

## Giai đoạn 4: Mô hình hóa & Dự báo (Tuần 4)
- [ ] Huấn luyện ARIMA & LSTM.
- [ ] Xây dựng 3 kịch bản tăng trưởng 2030 (Cơ sở, Lạc quan, Bi quan).
- [ ] Đánh giá khả năng vượt bẫy thu nhập trung bình theo từng kịch bản.

## Giai đoạn 5: Tổng hợp & Đề xuất (Tuần 5)
- [ ] Hoàn thiện Narrative.
- [ ] Đề xuất giải pháp cho các ngành Logistics, Tài chính, Du lịch dựa trên kết quả phân tích TFP.
- [ ] Hoàn thiện Notebook cuối cùng.

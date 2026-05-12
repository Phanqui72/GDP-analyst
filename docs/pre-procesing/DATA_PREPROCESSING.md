# Tài liệu Kỹ thuật: Tiền xử lý dữ liệu (Data Preprocessing)

## 1. Tổng quan
Giai đoạn tiền xử lý dữ liệu đóng vai trò then chốt trong việc chuyển đổi các tệp dữ liệu thô (raw data) từ nhiều nguồn khác nhau (Tổng cục Thống kê, World Bank, dữ liệu lịch sử tỷ giá) thành một cấu trúc chuẩn hóa, sẵn sàng cho việc phân tích sự chuyển dịch cơ cấu kinh tế và đóng góp của chỉ số TFP tại Việt Nam.

## 2. Quy trình xử lý chi tiết

### 2.1. Dữ liệu Sử dụng GDP (`Su_dung_GDP_Full.xlsx`)
- **Đặc điểm:** Tệp Excel có cấu trúc tiêu đề phức tạp, bao gồm cả các hàng cơ cấu (%) và các giá trị tuyệt đối. Tiêu đề năm chứa các ký tự không chuẩn (ví dụ: "So b 2024").
- **Kỹ thuật xử lý:**
    - Sử dụng `header=None` để đọc toàn bộ tệp và tự xử lý tiêu đề.
    - **Lọc hàng:** Chỉ giữ lại các hàng chứa giá trị tuyệt đối (tỷ đồng), loại bỏ các hàng cơ cấu (%) để tránh nhiễu dữ liệu.
    - **Chuẩn hóa cột năm:** Sử dụng logic tách chuỗi để lấy phần năm (ví dụ: "So b 2024" -> 2024).
    - **Xử lý giá trị thiếu:** Chuyển đổi các ký tự ".." thành `NaN` và ép kiểu về `float64`.
    - **Chuyển vị (Transpose):** Chuyển đổi dữ liệu từ dạng chiều ngang (năm là cột) sang chiều dọc (năm là hàng) để phù hợp với phân tích chuỗi thời gian.

### 2.2. Dữ liệu Cơ cấu GDP theo khu vực (`Co_cau_GDP_theo_khu_vuc_Full.xlsx`)
- **Đặc điểm:** Chứa giá trị GDP của 3 khu vực kinh tế chính: Nông lâm thủy sản (Khu vực I), Công nghiệp & Xây dựng (Khu vực II), và Dịch vụ (Khu vực III).
- **Kỹ thuật xử lý:**
    - Loại bỏ các cột "Cơ cấu (%)" để tập trung vào giá trị tuyệt đối.
    - Chuẩn hóa cột "Năm" và xử lý các ký tự đặc biệt trong dữ liệu dự báo (Sơ bộ).
    - Xử lý cột "Thuế sản phẩm" (thường chứa giá trị thiếu trong các năm cũ) bằng cách chuyển đổi sang kiểu `numeric` và giữ `NaN` thay vì điền sai lệch.

### 2.3. Đóng góp của TFP (`Dong_gop_TFP_Full.xlsx`)
- **Đặc điểm:** Dữ liệu TFP thường được báo cáo theo giai đoạn (ví dụ: 2011-2015), trong khi các dữ liệu khác theo từng năm.
- **Kỹ thuật xử lý (Key Insight):**
    - **Mở rộng (Expansion):** Sử dụng vòng lặp để giải nén các giai đoạn thành từng năm đơn lẻ. Điều này cho phép khớp dữ liệu TFP với các chỉ số GDP hàng năm mà không làm mất đi tính liên tục của dữ liệu.
    - Thiết lập "Năm" làm chỉ mục (Index) để tối ưu hóa việc liên kết (Join/Merge) sau này.

## 3. Đánh giá chất lượng tiền xử lý
Dựa trên tiêu chuẩn của một kỹ sư dữ liệu, các bước xử lý hiện tại đạt chất lượng **Tốt** nhờ:
1.  **Tính linh hoạt:** Xử lý được các cấu trúc Excel không chuẩn.
2.  **Tính chính xác:** Loại bỏ đúng các hàng/cột nhiễu (Cơ cấu %).
3.  **Tư duy phân tích:** Việc "unfold" dữ liệu TFP từ giai đoạn sang năm là một kỹ thuật xử lý dữ liệu thời gian chính xác.
4.  **Sẵn sàng cho sản xuất:** Các đường dẫn đã được chuẩn hóa sang cấu trúc project local và tự động xuất kết quả ra `data/processed/`.

## 4. Các bước đề xuất tiếp theo
Để hoàn thiện bộ dữ liệu tổng thể, cần thực hiện thêm các bước sau:
- **Tích hợp Tỷ giá (USD/VND):** Tổng hợp dữ liệu tỷ giá hàng ngày thành trung bình năm để quy đổi GDP sang USD, phục vụ so sánh quốc tế.
- **Tiền xử lý World Bank Data:** Xử lý tệp `world_bank.csv` bằng cách trích xuất năm từ tiêu đề cột (ví dụ: `1986 [YR1986]` -> `1986`).
- **Hợp nhất (Master Join):** Thực hiện `pd.concat` hoặc `pd.merge` tất cả các DataFrame trong thư mục `processed` vào một tệp `master_dataset.csv` duy nhất.

---
*Tài liệu được biên soạn bởi Kỹ sư Dữ liệu Dự án GDP-Analyst.*

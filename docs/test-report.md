# Báo cáo Kết quả Kiểm thử (Test Report)

## 1. Tóm tắt Thực thi
- **Ngày kiểm thử**: 27/09/2026
- **Môi trường**: Windows 11, Node.js v22, MS SQL Server, Python 3.13 Flask (port 5001), Vite Frontend (port 3000).
- **Tổng số ca kiểm thử**: 5
- **Đạt (Pass)**: 5 / 5 (100%)
- **Không đạt (Fail)**: 0

## 2. Chi tiết Kết quả Kiểm thử

| Mã TC | Mô tả | Trạng thái | Ghi chú bằng chứng |
| :--- | :--- | :--- | :--- |
| **TC-001** | Chatbot tìm kiếm theo khoảng giá | **PASS** | Bóc tách chính xác maxPrice = 15.000.000, trả về sản phẩm `iPhone 11 64GB - Chính Hãng Apple (11.490.000 VNĐ)`. |
| **TC-002** | Thêm sản phẩm vào giỏ hàng | **PASS** | Gọi thành công `CartRepository.addItemToCart`, giỏ hàng cập nhật số lượng chính xác. |
| **TC-003** | Lấy danh sách sản phẩm | **PASS** | Trả về 50 model iPhone và phụ kiện chính hãng Apple trong CSDL kèm danh mục. |
| **TC-004** | Lấy danh mục sản phẩm | **PASS** | Trả về các danh mục thế hệ iPhone (iPhone 18 Series, 17 Series, 16 Series, 15 Series, Cổ Điển...). |
| **TC-005** | API Danh sách AI Skills | **PASS** | Trả về 13 kỹ năng AI chuẩn hóa (Multi-Agent RAG, Spec Compare, Stock Copilot, POS Assistant...). |

## 3. Kết luận
Toàn bộ các luồng chức năng trọng yếu của hệ thống đã hoạt động ổn định và đạt 100% tiêu chí chấp nhận.

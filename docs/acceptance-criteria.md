# Tiêu chí Chấp nhận (Acceptance Criteria)

### AC-001: Tìm kiếm Sản phẩm bằng AI Chatbot (US-004)
- **Kịch bản 1: Tìm kiếm theo khoảng giá & dòng máy**
  - **Given**: Khách hàng mở cửa sổ Chatbot ZShop.
  - **When**: Khách hàng nhập tin nhắn "tìm iphone dưới 15 triệu".
  - **Then**: Hệ thống bóc tách `max_price = 15000000` và `keyword = 'iphone'`.
  - **And**: Chatbot trả về danh sách các model iPhone có giá `<= 15.000.000 VNĐ` kèm nút "Thêm vào giỏ" và "Xem chi tiết".
- **Kịch bản 2: Không tìm thấy sản phẩm**
  - **Given**: Khách hàng hỏi sản phẩm không tồn tại trong hệ thống.
  - **When**: Khách hàng hỏi "tìm phi thuyền vũ trụ".
  - **Then**: Chatbot thông báo lịch sự không tìm thấy sản phẩm trong kho và gợi ý các dòng iPhone chính hãng đang có sẵn.

### AC-002: Thêm vào giỏ hàng và Đồng bộ (US-002)
- **Given**: Khách hàng đang ở trang sản phẩm hoặc thẻ sản phẩm của Chatbot.
- **When**: Nhấn nút "Thêm vào giỏ".
- **Then**: Số lượng hiển thị trên MiniCart tăng lên ngay lập tức (Optimistic Update).
- **And**: Gửi yêu cầu `POST /api/carts/add` lưu thông tin vào bảng `CartItems` trong cơ sở dữ liệu.

### AC-003: Quản lý & Cập nhật sản phẩm bởi Quản trị viên / Thủ kho (US-006, US-007)
- **Given**: Sản phẩm iPhone hoặc phụ kiện mới cần bổ sung vào kho.
- **When**: Nhân viên kho hoặc Admin đăng nhập vào Dashboard và lưu thông tin sản phẩm.
- **Then**: CSDL cập nhật thông tin máy, giá niêm yết và tồn kho thực tế.
- **And**: Sản phẩm hiển thị ngay lập tức trên trang chủ và sẵn sàng bán.

# Tài liệu Phân tích Câu hỏi (Question Analysis)

## 1. Mục tiêu Module
Chuyển hóa câu hỏi bằng ngôn ngữ tự nhiên thành một cấu trúc JSON xác định (Structured Intent) để làm tham số cho các bộ lọc truy vấn CSDL và RAG Vector Store.

## 2. Các Mẫu Biểu thức Chính Quy (Regex Patterns)
- **Khoảng giá dưới X**: `dưới\s+(\d+(?:\.\d+)?)\s*(k|nghìn|ngàn|triệu|tr|m)?`
  - Ví dụ: "dưới 15 triệu" -> `max_price = 15000000`
- **Khoảng giá trên / từ X**: `(?:trên|từ)\s+(\d+(?:\.\d+)?)\s*(k|nghìn|ngàn|triệu|tr|m)?`
  - Ví dụ: "từ 20 triệu" -> `min_price = 20000000`
- **Khoảng giá xấp xỉ / tầm X**: `(?:tầm|khoảng)\s+(\d+(?:\.\d+)?)\s*(k|nghìn|ngàn|triệu|tr|m)?`
  - Ví dụ: "tầm 25 triệu" -> `min_price = 22000000, max_price = 28000000`

## 3. Danh mục Từ khóa Nhận diện (Thế Giới iPhone)
- `keywords`: `['iphone', 'ip', 'pro max', 'promax', 'pro', 'plus', 'air', 'ultra', 'sạc', 'tai nghe', 'airpods', 'magsafe', 'ốp lưng', 'cáp']`
- `categories`: `['iPhone 18 Series (Flagship 2026)', 'iPhone 17 Series', 'iPhone 16 Series', 'iPhone 15 Series', 'iPhone 14 Series', 'iPhone 13 Series', 'iPhone Cổ Điển & Sưu Tầm', 'Phụ Kiện Apple Chính Hãng']`

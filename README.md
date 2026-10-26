# 📱 Thế Giới iPhone — ZShop
### Hệ Thống Quản Lý Bán Hàng & Thương Mại Điện Tử Tích Hợp AI Multi-Agent RAG

[![React 19](https://img.shields.io/badge/React-19.2-61dafb?style=for-the-badge&logo=react)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178C6?style=for-the-badge&logo=typescript)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-6.2-646CFF?style=for-the-badge&logo=vite)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38B2AC?style=for-the-badge&logo=tailwind-css)](https://tailwindcss.com/)
[![Node.js](https://img.shields.io/badge/Node.js-Express_v5-green?style=for-the-badge&logo=node.js)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-Flask_Microservice-yellow?style=for-the-badge&logo=python)](https://python.org/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-red?style=for-the-badge)](https://www.trychroma.com/)

---

## 🌟 Giới Thiệu Dự Án (Project Overview)

**Thế Giới iPhone — ZShop** là giải pháp phần mềm quản trị bán hàng và thương mại điện tử thông minh, vận hành theo mô hình **Cửa hàng Đơn nhất (Single-Store Model)** chuyên biệt cho các dòng **Điện thoại iPhone chính hãng Apple VN/A & Máy Sưu Tầm** (từ iPhone 4s, 8 Plus, XS Max, 11, 12, 13, 14, 15, 16, 17 đến iPhone 18 Pro Max Flagship) cùng hệ sinh thái phụ kiện Apple cao cấp.

Hệ thống tích hợp công nghệ **Multi-Agent RAG AI** (8 tác tử thông minh), kiến trúc phân quyền chuẩn **UML 2.5 cho 4 tác nhân**, cổng thanh toán trực tuyến **SZ-Payment (VietQR Napas 24/7)** và cơ sở dữ liệu quan hệ **15 bảng chuẩn 3NF**.

---

## 👥 Mô Hình 4 Tác Nhân Chuẩn UML 2.5 (RBAC Matrix)

Hệ thống phân định rành mạch quyền hạn và không gian làm việc giữa 4 vai trò:

1. **Admin (`ADMIN`) — Chủ cửa hàng**:
   - Giám sát dashboard kinh doanh tổng thể: Doanh thu tuần/tháng, tỷ suất lợi nhuận, biểu đồ đơn hàng.
   - Quản trị nhân sự: Phê duyệt và cấp quyền cho Nhân viên Bán hàng và Nhân viên Kho.
   - Báo cáo tài chính AI BI (`UC09`): Dự báo doanh số, xuất báo cáo doanh thu Excel/PDF.

2. **Nhân viên Bán hàng (`SALES`) — POS & CSKH**:
   - Phân hệ bán lẻ tại quầy POS (`UC04`): Quét mã sản phẩm, tra cứu SĐT khách hàng, tự động tính chiết khấu VIP và in hóa đơn tức thì.
   - Quản lý CRM & Khách hàng thân thiết (`UC03`): Tra cứu lịch sử mua sắm, hạng thành viên (Đồng, Bạc, Vàng, Kim Cương).
   - Tiếp nhận & duyệt đổi trả 1-1 (`UC10`): Tự động thu hồi điểm tích lũy tương ứng theo quy định.

3. **Nhân viên Kho (`WAREHOUSE`) — Quản lý Sản phẩm & Tồn kho**:
   - Quản lý danh mục máy & phụ kiện (`UC02`): Cập nhật giá bán, số lượng tồn kho thực tế.
   - Lập phiếu nhập kho (`UC05`): Nhập lô máy VN/A từ nhà cung cấp ủy quyền.
   - AI Dự báo & Khuyến nghị Nhập kho (`UC08`): Cảnh báo ngưỡng tồn kho an toàn (`stock <= 25 máy`) và tự động đề xuất số lượng nhập tối ưu.

4. **Khách hàng (`CUSTOMER`) — Mua sắm Trực tuyến**:
   - Khám phá showroom máy qua giao diện Bento Grid trực quan (`UC02`).
   - Mua sắm giỏ hàng thông minh, chọn mua lẻ từng máy hoặc theo nhóm dòng máy.
   - Thanh toán đa kênh **SZ-Payment** (`VietQR Napas 24/7`, `COD`, `Thẻ quốc tế`).
   - Đối thoại với **Trợ lý AI GenZ Copilot** (`UC07`): Tra cứu cấu hình chip A-Series, camera, pin, so sánh máy, kiểm tra đơn hàng và quyền lợi VIP.

---

## 🧠 Kiến Trúc Multi-Agent RAG AI (8 Agents Pipeline)

Hệ thống AI Microservice vận hành tại `agent_service/` kết nối Vector DB **ChromaDB**:

1. **Orchestrator Agent**: Điều phối luồng xử lý toàn cục và phân định ngữ cảnh câu hỏi.
2. **Analyst Agent**: Phân tích ý định tự nhiên, trích xuất thực thể (model máy, dung lượng, màu sắc, khoảng giá) và giải mã tiếng lóng GenZ Việt Nam.
3. **Database Agent**: Truy vấn an toàn CSDL MySQL/SQL Server, kiểm tra giá và tồn kho thời gian thực.
4. **RAG Agent**: Tìm kiếm tri thức ngữ nghĩa từ ChromaDB (thông số kỹ thuật, bảo hành chính hãng, chính sách đổi trả).
5. **Recommendation Agent**: Gợi ý các model máy phù hợp nhất theo ngân sách và nhu cầu công thái học.
6. **Reasoning Agent**: Lập luận so sánh chuyên sâu (chip, màn hình Promotion 120Hz, camera tele zoom, thời lượng pin).
7. **Critic Agent**: Kiểm định phản hồi, ngăn chặn ảo giác giá (0% Hallucination) và bảo đảm dữ liệu luôn khớp kho thực tế.
8. **Response Agent**: Định dạng câu trả lời thân thiện, sinh thẻ sản phẩm tương tác và đề xuất nút hành động 1-click.

---

## 🛠️ Công Nghệ Sử Dụng (Tech Stack)

| Hạng mục | Công nghệ |
| :--- | :--- |
| **Giao diện (Frontend)** | React 19, TypeScript 5.8, Vite 6.2, Tailwind CSS 3.4, Lucide React |
| **Dịch vụ Nghiệp vụ (Backend)** | Node.js, Express v5, MSSQL / MySQL Client, JWT, CORS |
| **Trí tuệ Nhân tạo (AI Microservice)** | Python 3.10+, Flask, ChromaDB, Sentence-Transformers, Google Gemini API |
| **Cơ sở Dữ liệu (Database)** | SQL Server / MySQL (15 bảng chuẩn 3NF), Vector DB ChromaDB |
| **Cổng thanh toán (Payment)** | SZ-Payment Gateway (VietQR Napas 24/7, MoMo, COD) |

---

## 📁 Cấu Trúc Thư Mục (Project Structure)

```text
_Web_ZShop-main/
├── agent_service/               # AI Microservice (Python Flask + ChromaDB)
│   ├── agents/                  # 8 Tác tử AI (Orchestrator, Analyst, RAG, Critic...)
│   ├── data/                    # all_50_products.json & Chroma Vector Store
│   └── run_server.py            # Entry point chạy AI Microservice (Port 5001)
├── components/                  # Giao diện người dùng React 19
│   ├── ZShop/                   # Storefront (Header, ShopeeHomePage, ProductGrid...)
│   ├── AdminDashboard.tsx       # Phân hệ Quản trị Chủ cửa hàng (ADMIN)
│   ├── CSKHPortalPage.tsx       # Phân hệ POS & CSKH Nhân viên Bán hàng (SALES)
│   ├── WarehousePage.tsx        # Phân hệ Kho & Nhập kho VN/A (WAREHOUSE)
│   ├── ChatBot.tsx              # Trợ lý AI Bán hàng GenZ Copilot
│   ├── CheckoutPage.tsx         # Thanh toán 1 trang SZ-Payment
│   ├── MiniCart.tsx             # Giỏ hàng thông minh
│   ├── MyOrdersPage.tsx         # Tra cứu đơn hàng & Đổi trả 1-1
│   └── ProductDetailPage.tsx    # Chi tiết sản phẩm & so sánh cấu hình
├── szshop-backend/              # Backend API (Node.js Express v5)
│   ├── controllers/             # Auth, Product, Cart, Order, Payment, Chat Controller
│   ├── repositories/            # Data Access Layer (SQL Server / MySQL)
│   ├── services/                # Nghiệp vụ & AiService (Fallback RAG)
│   ├── database.sql             # Kịch bản khởi tạo 15 bảng CSDL chuẩn 3NF
│   └── server.js                # Entry point Express API (Port 5000)
├── App.tsx                      # Bộ điều hướng ViewState & Phân quyền 4 Tác nhân
├── database.ts                  # Mock CSDL & Data Adapter cho Storefront
├── constants.ts                 # Danh mục 50 mã iPhone & Phụ kiện chuẩn Apple
└── tailwind.config.js           # Palette Titanium Vàng Sa Mạc (#9a7b4f) & Font Inter
```

---

## 🚀 Hướng Dẫn Cài Đặt & Khởi Chạy (Getting Started)

### Yêu Cầu Tiên Quyết
* **Node.js**: Phiên bản 18.x trở lên.
* **Python**: Phiên bản 3.10 trở lên.
* **SQL Server** hoặc **MySQL**: Đã cài đặt hoặc chạy qua Docker.

### 1. Cài đặt dependencies Frontend & Backend
```bash
# Cài đặt thư viện Frontend
npm install

# Cài đặt thư viện Backend
cd szshop-backend
npm install
cd ..
```

### 2. Cài đặt môi trường AI Microservice
```bash
cd agent_service
pip install -r requirements.txt # hoặc flask pymysql chromadb sentence-transformers
cd ..
```

### 3. Khởi chạy toàn bộ hệ sinh thái
Hệ thống cung cấp sẵn script chạy đồng thời qua `concurrently`:
```bash
# Chạy đồng thời Backend (5000) và Frontend Vite (3000):
npm run dev:all

# Hoặc chạy đầy đủ cả 3 tầng (Backend 5000 + AI Microservice 5001 + Frontend 3000):
npm run dev:full
```

Truy cập hệ thống tại: 👉 **`http://localhost:3000`**

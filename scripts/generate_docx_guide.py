# -*- coding: utf-8 -*-
"""
Script tạo file tài liệu Word (.docx) Cẩm nang Vấn đáp Đồ án AI - Hệ thống Thế Giới iPhone (ZShop)
Phục vụ bảo vệ đồ án kết thúc học phần Thực hành AI-Augmented SDLC
"""
import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="D1D5DB", sz="4", val="single"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def build_docx(output_path):
    doc = docx.Document()

    # Thiết lập lề trang chuẩn (Top/Bottom: 2cm, Left/Right: 2cm)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Style colors
    PRIMARY = RGBColor(27, 54, 93)      # Navy Blue #1B365D
    SECONDARY = RGBColor(13, 148, 136)  # Teal #0D9488
    DARK_TEXT = RGBColor(30, 41, 59)    # Slate 800 #1E293B
    MUTED_TEXT = RGBColor(100, 116, 139)# Slate 500 #64748B
    HIGHLIGHT = RGBColor(180, 83, 9)    # Amber 700

    # 1. TIÊU ĐỀ TRANG BÌA / HEADER TRANG TRỌNG
    p_header = doc.add_paragraph()
    p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sch = p_header.add_run("KHOA CÔNG NGHỆ THÔNG TIN - TRƯỜNG ĐẠI HỌC CNTT & TRUYỀN THÔNG (ICTU)\n")
    run_sch.font.name = "Arial"
    run_sch.font.size = Pt(11)
    run_sch.font.bold = True
    run_sch.font.color.rgb = MUTED_TEXT

    run_sub = p_header.add_run("HỌC PHẦN: THỰC HÀNH PHÁT TRIỂN PHẦN MỀM CÓ AI HỖ TRỢ (AI-AUGMENTED SDLC)\n")
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(11)
    run_sub.font.bold = True
    run_sub.font.color.rgb = SECONDARY

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_main_title = p_title.add_run("CẨM NANG TOÀN DIỆN VẤN ĐÁP ĐỒ ÁN AI\n")
    run_main_title.font.name = "Arial"
    run_main_title.font.size = Pt(20)
    run_main_title.font.bold = True
    run_main_title.font.color.rgb = PRIMARY

    run_proj = p_title.add_run("HỆ THỐNG THẾ GIỚI IPHONE (ZSHOP) - SINGLE-STORE 3D RETAIL & MULTI-AGENT RAG")
    run_proj.font.name = "Arial"
    run_proj.font.size = Pt(13)
    run_proj.font.bold = True
    run_proj.font.color.rgb = SECONDARY

    # Khung Thông tin nhóm
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_meta = p_meta.add_run(
        "Nhóm thực hiện: Nhóm 01 | Nhóm 2 Sinh viên\n"
        "Trưởng nhóm: Nguyễn Quốc Khánh (MSSV: DTC245220042) - Phụ trách Backend, CSDL 3NF, SZ-Payment, Multi-Agent RAG Python & Critic Gate\n"
        "Thành viên: Mẫn Bá Hảo - Phụ trách Storefront React 19, 3D Canvas, Portal 4 Vai trò, Giỏ hàng & Luồng Đổi trả/Nhập kho\n"
        "Thời gian vấn đáp: Ngày 29/10/2026 | Phiên bản hệ thống: V2.0 (Đồng bộ 100% mã nguồn thực tế)"
    )
    run_meta.font.name = "Arial"
    run_meta.font.size = Pt(9.5)
    run_meta.font.italic = True
    run_meta.font.color.rgb = MUTED_TEXT

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = PRIMARY
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = SECONDARY
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = DARK_TEXT
        return p

    def add_body(text, bold_prefix=None, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.font.name = "Arial"
            r_b.font.size = Pt(10)
            r_b.font.bold = True
            r_b.font.color.rgb = DARK_TEXT
        r_t = p.add_run(text)
        r_t.font.name = "Arial"
        r_t.font.size = Pt(10)
        r_t.font.italic = italic
        r_t.font.color.rgb = DARK_TEXT
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.font.name = "Arial"
            r_b.font.size = Pt(10)
            r_b.font.bold = True
            r_b.font.color.rgb = DARK_TEXT
        r_t = p.add_run(text)
        r_t.font.name = "Arial"
        r_t.font.size = Pt(10)
        r_t.font.color.rgb = DARK_TEXT
        return p

    def add_callout(text, bold_title="LƯU Ý QUAN TRỌNG:"):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        cell = table.cell(0, 0)
        cell.width = Inches(6.8)
        set_cell_background(cell, "EFF6FF") # Blue light
        set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
        tcPr = cell._element.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="2563EB"/>'
            f'  <w:top w:val="none"/>'
            f'  <w:bottom w:val="none"/>'
            f'  <w:right w:val="none"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        rb = p.add_run(bold_title + " ")
        rb.font.name = "Arial"
        rb.font.size = Pt(10)
        rb.font.bold = True
        rb.font.color.rgb = RGBColor(29, 78, 216)
        rt = p.add_run(text)
        rt.font.name = "Arial"
        rt.font.size = Pt(10)
        rt.font.color.rgb = DARK_TEXT
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # =========================================================================
    # PHẦN I: GIẢI MÃ BẢN CHẤT 2 ẢNH TIÊU CHÍ CHẤM THI
    # =========================================================================
    add_h1("PHẦN I: GIẢI MÃ BẢN CHẤT 2 ẢNH TIÊU CHÍ CHẤM THI")
    add_body(
        "Hai ảnh tiêu chí trong thư mục 'E:\\Tiêu chí AI' thực chất là hai văn bản quy chuẩn bổ trợ cho nhau của Khoa Công nghệ thông tin: "
        "Ảnh 1 là Khung đánh giá tổng thể môn học (Báo cáo 3đ + Sản phẩm do AI tạo ra 7đ, trong đó Thiết kế Agent AI cho SDLC chiếm 4đ). "
        "Ảnh 2 là Phiếu chấm vấn đáp trực tiếp gồm 5 tiêu chí độc lập (mỗi tiêu chí 2.0đ = 10 điểm) mà Ban giám khảo sẽ cầm trên tay để đặt câu hỏi cho sinh viên."
    )

    # Bảng so sánh 2 ảnh
    tbl_comp = doc.add_table(rows=5, cols=4)
    tbl_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_comp.autofit = False
    set_table_borders(tbl_comp)

    headers = ["Hạng mục", "Ảnh 1: Cấu trúc Thang điểm Chung (10đ)", "Ảnh 2: Tiêu chí Vấn đáp Chi tiết (5 x 2.0 = 10đ)", "Trọng số & Ý nghĩa"]
    col_widths = [Inches(1.2), Inches(2.0), Inches(2.4), Inches(1.2)]

    for j, h in enumerate(headers):
        cell = tbl_comp.cell(0, j)
        cell.width = col_widths[j]
        set_cell_background(cell, "1E3A8A") # Navy header
        set_cell_margins(cell, top=140, bottom=140, left=140, right=140)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_rows = [
        ("Nghiệp vụ & Giải pháp", "Tiêu chí 1: Quyển báo cáo (3.0đ) - Phân tích nghiệp vụ (1.1), Chức năng (1.2), Kiến trúc/CSDL (1.3)", "Tiêu chí 1 (2.0đ) - 1.1 Đúng nghiệp vụ; 1.2 Chức năng đầy đủ; 1.3 Kiến trúc/CSDL; 1.4 Lý giải vị trí AI", "CLO1 (20% - 30%)\nĐánh giá nền tảng"),
        ("Sản phẩm & Chức năng AI", "Tiêu chí 2 (mục 1): Hoàn thiện hệ thống và chức năng AI (2.0đ)", "Tiêu chí 2 (2.0đ) - 2.1 Nghiệp vụ chạy đúng; 2.2 Đăng nhập & phân quyền; 2.3 AI phục vụ nghiệp vụ; 2.4 API & Prompt", "CLO2, CLO3 (20%)\nĐánh giá tính năng"),
        ("TRỌNG TÂM: Agent AI SDLC", "Tiêu chí 2 (mục 2): Thiết kế Agent AI cho SDLC (4.0đ) - Context engineering, factory, unit/integration test, guardrails, bảo mật -> Vận hành như nhà máy phần mềm", "Phân rã thành Tiêu chí 3 (Kiểm thử, đánh giá, bảo mật 2.0đ) và Tiêu chí 5 (SDLC & Tư duy phản biện 2.0đ)", "CLO3, CLO4, CLO5 (40%)\nQUYẾT ĐỊNH ĐIỂM GIỎI"),
        ("Vận hành & Demo", "Tiêu chí 2 (mục 3): Đóng gói, vận hành & theo dõi sản phẩm (1.0đ)", "Tiêu chí 4 (2.0đ) - 4.1 UI dễ dùng; 4.2 Triển khai Git/README; 4.3 Báo cáo kỹ thuật; 4.4 Demo trực tiếp", "CLO1, CLO5 (10% - 20%)\nĐánh giá thực nghiệm")
    ]

    for i, row in enumerate(data_rows):
        bg = "F8FAFC" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            cell = tbl_comp.cell(i + 1, j)
            cell.width = col_widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(9)
            r.font.color.rgb = DARK_TEXT
            if j == 0 or (i == 2 and j == 3):
                r.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # =========================================================================
    # PHẦN II: BỘ CÂU TRẢ LỜI ĐẠT ĐIỂM TỐI ĐA (10/10) THEO HỆ THỐNG ZSHOP
    # =========================================================================
    add_h1("PHẦN II: BỘ CÂU TRẢ LỜI ĐẠT ĐIỂM TỐI ĐA (10/10) THEO HỆ THỐNG ZSHOP")

    # TIÊU CHÍ 1
    add_h2("TIÊU CHÍ 1: PHÂN TÍCH BÀI TOÁN VÀ THIẾT KẾ GIẢI PHÁP (CLO1 - 2.0đ / 3.0đ)")
    add_bullet(
        "ZShop vận hành theo mô hình Cửa hàng bán lẻ đơn nhất (Single-Store Model), chuyên phân phối các dòng iPhone chính hãng VN/A và phụ kiện Apple cao cấp. Hệ thống loại bỏ mô hình sàn đa người bán (Multi-vendor) phức tạp, tập trung tối ưu hóa 10 Use Case nghiệp vụ chuẩn hóa (UC01 đến UC10) với quy trình nhập kho có kiểm soát và bán hàng đa kênh (Online + POS tại quầy).",
        "1.1 Phân tích đúng nghiệp vụ: "
    )
    add_bullet(
        "Hệ thống phân quyền theo ma trận RBAC với 4 tác nhân chuẩn UML 2.5: (1) CUSTOMER: Mua sắm 3D, chat AI, đặt hàng, tích điểm VIP; (2) SALES: Nhân viên bán hàng tại quầy POS, tra cứu CRM VIP, duyệt đổi trả 1-1; (3) WAREHOUSE: Lập phiếu nhập kho chuẩn NK-YYYY-XXXX, kiểm kho, sử dụng AI Stock Copilot; (4) ADMIN: Toàn quyền quản trị, xem báo cáo doanh thu và ra quyết định cùng AI BI. Yêu cầu phi chức năng (NFR): Tốc độ phản hồi API < 500ms, cơ chế 3-Tier Smart Offline Fallback đảm bảo vận hành 100% không gián đoạn.",
        "1.2 Yêu cầu chức năng & phi chức năng đầy đủ: "
    )
    add_bullet(
        "Hệ thống xây dựng theo Kiến trúc 4 tầng rời (Layered Architecture): Presentation Layer (React 19 + TypeScript + Three.js), API Layer (Node.js Express v5 - Port 5000), AI Microservice Layer (Python Flask + ChromaDB - Port 5001), và Database Layer (Microsoft SQL Server chuẩn 3NF với 11-15 bảng: Roles, Users, Customers, Staffs, Products, StockImportTickets, Orders, Payments, ReturnRequests; song hành cùng ChromaDB Vector DB 384 chiều).",
        "1.3 Kiến trúc và CSDL hợp lý: "
    )
    add_bullet(
        "Nhóm chủ động tách AI thành một Microservice Python độc lập vì 3 lý do chiến lược: (1) Python sở hữu hệ sinh thái AI vượt trội (ChromaDB, NLP, Sentence-Transformers); (2) Tách biệt tải trọng (Decoupling) giúp tầng bán hàng Node.js duy trì tốc độ xử lý đơn hàng cao mà không bị nghẽn bởi các tác vụ suy luận LLM; (3) Khả năng mở rộng độc lập (Independent Scalability) cho phép đưa cụm AI lên container GPU khi lượng truy cập tăng vọt.",
        "1.4 Lý giải vị trí AI trong hệ thống (Điểm sáng lý thuyết): "
    )

    # TIÊU CHÍ 2
    add_h2("TIÊU CHÍ 2: HOÀN THIỆN HỆ THỐNG VÀ CHỨC NĂNG AI (CLO2, CLO3 - 2.0đ)")
    add_bullet(
        "Toàn bộ luồng thương mại điện tử vận hành trơn tru: Khách chọn iPhone -> Giỏ hàng thông minh (MiniCart) -> Áp mã voucher -> Cổng thanh toán SZ-Payment (VietQR Napas 247) -> Hệ thống tự động trừ kho và sinh mã vận đơn DH-XXXXXXXX. Nhân viên bán hàng tạo đơn POS tại quầy, nhân viên kho tạo phiếu nhập hàng làm tăng tồn kho tức thì.",
        "2.1 Nghiệp vụ chính chạy đúng: "
    )
    add_bullet(
        "Hệ thống cài đặt 4 tài khoản phân quyền chuẩn để kiểm thử: customer@test.com (Khách hàng), sales@test.com (Nhân viên CSKH/POS), warehouse@test.com (Nhân viên kho), và admin@test.com (Admin - Chủ shop). Mọi đường dẫn và API đều có Role Guard chặn truy cập trái phép.",
        "2.2 Đăng nhập và phân quyền (RBAC): "
    )
    add_bullet(
        "Hệ thống tích hợp 13 kỹ năng AI (định nghĩa tại aiSkills.ts). Giao diện ChatBot chia 4 Tab chuyên sâu: STYLIST (Tư vấn phối combo công sở/gaming), FITTING (So sánh thông số chip A18 Pro, màn hình ProMotion 120Hz), ORDERS (Tra cứu hành trình vận đơn), VIP (Tra cứu tích điểm đổi quà). Ngoài ra có 2 kỹ năng AI nội bộ: AI Stock Copilot (cảnh báo khi stock <= 40) và AI Business Intelligence (phân tích lợi nhuận cho chủ cửa hàng).",
        "2.3 AI phục vụ nghiệp vụ trực tiếp: "
    )
    add_bullet(
        "Chatbot UI gọi REST endpoint POST /api/chat. Nhóm áp dụng kỹ thuật Context Engineering: Đóng gói tin nhắn cùng Persona hiện tại, thông tin hạng thẻ VIP của khách và giỏ hàng hiện tại vào payload. Prompt được thiết kế theo cơ chế Grounding, ràng buộc AI chỉ trả lời dựa trên tri thức thực tế trích xuất từ ChromaDB và SQL.",
        "2.4 Kết nối API và Prompt Engineering: "
    )

    # TRỌNG TÂM 4 ĐIỂM
    add_h2("TRỌNG TÂM 4 ĐIỂM: THIẾT KẾ AGENT AI CHO QUY TRÌNH SDLC & KIỂM THỬ (ẢNH 1 MỤC 2.2 / ẢNH 2 TIÊU CHÍ 3 & 5)")
    add_callout(
        "Đây là phần chiếm tới 4.0 điểm trong đề thi! Giám khảo muốn thấy bạn chứng minh hệ thống vận hành như một 'Nhà máy phát triển phần mềm' (SDLC Factory) kết hợp với Cơ chế rào chắn an toàn (Guardrails) và Vòng lặp phản hồi (Reflection Loop) tự sửa lỗi.",
        "TRỌNG TÂM CHIẾN LƯỢC ĐẠT ĐIỂM 10:"
    )

    add_h3("A. Nhà máy phát triển phần mềm (AI-Augmented SDLC Factory)")
    add_body(
        "Dự án ZShop không chỉ áp dụng AI cho ứng dụng cuối mà toàn bộ quá trình phát triển được tự động hóa qua hệ thống 'Dây chuyền Agent' tại thư mục .agents/skills/ gồm 13 skills chuẩn hóa:"
    )
    add_bullet("Phân tích yêu cầu tự nhiên thành Functional Requirements (FR-001..FR-005), NFR, User Stories và Acceptance Criteria.", "1. requirements-analysis: ")
    add_bullet("Thiết kế kiến trúc phân tầng 4 lớp, lập Architectural Decision Records (ADR-001 RAG, ADR-002 Decoupling).", "2. architecture-design: ")
    add_bullet("Thiết kế CSDL quan hệ chuẩn 3NF 11 bảng, DDL script, indexing và ràng buộc toàn vẹn khóa ngoại.", "3. database-design: ")
    add_bullet("Sinh mã nguồn Frontend React 19 và Backend Node.js bám sát tiêu chuẩn Clean Architecture.", "4. implementation: ")
    add_bullet("Rà soát chất lượng code, kiểm tra lỗ hổng SQL Injection, XSS, CORS và bảo vệ Secret Key.", "5. code-review & security-review: ")
    add_bullet("Lập Test Plan, xây dựng Test Cases theo phương pháp phân tích giá trị biên (BVA) và phân hoạch tương đương.", "6. testing: ")
    add_bullet("Tự động đồng bộ tài liệu kỹ thuật SRS (97KB), cẩm nang triển khai và hướng dẫn vấn đáp.", "7. documentation: ")

    add_h3("B. Kiến trúc 8 Agents & Rào chắn an toàn chống ảo giác (0% Hallucination)")
    add_body(
        "Trong agent_service/app.py và agent_service/agents/orchestrator.py, luồng xử lý câu hỏi của khách hàng được phối hợp qua Structured Message Bus theo quy trình nghiêm ngặt:"
    )
    add_bullet("Tiếp nhận câu hỏi, gán correlation_id định danh luồng xử lý và phát lệnh lên Message Bus.", "1. Orchestrator Agent: ")
    add_bullet("Phân tích ý định (Intent: PRODUCT_SEARCH, FASHION_OUTFIT...) và bóc tách thực thể (model, max_price, category).", "2. Analyst Agent: ")
    add_bullet("Truy vấn song song: Database Agent truy vấn CSDL MySQL; RAG Agent truy vấn Vector DB ChromaDB lấy 50 vector sản phẩm.", "3. Database & RAG Agents: ")
    add_bullet("Tính toán gợi ý bán chéo (Cross-sell: khách mua iPhone gợi ý củ sạc GaN 65W, ốp lưng MagSafe).", "4. Recommendation Agent: ")
    add_bullet("Tổng hợp thông tin từ RAG và CSDL để soạn thảo bản thảo câu trả lời (Draft Message).", "5. Reasoning Agent: ")
    add_bullet("Đóng vai trò CỔNG GÁC KIỂM ĐỊNH ĐỘC LẬP (Critic Gate) với 4 tầng rào chắn: (1) Kiểm tra ID và giá thực tế; (2) Ép trần ngân sách (nếu khách hỏi dưới 15 triệu mà có máy 16 triệu lọt vào -> lập tức chặn lại); (3) Kiểm tra bối cảnh sử dụng; (4) Nếu vi phạm, Critic phát cờ REVISE kèm phản hồi cụ thể.", "6. Critic Agent (Guardrails): ")
    add_bullet("Khi Critic phát cờ REVISE, hệ thống tự động kích hoạt vòng lặp Reflection Loop (tối đa 2 vòng). Reasoning Agent nhận feedback của Critic, truy xuất lại dữ liệu đúng và viết lại câu trả lời cho đến khi đạt cờ ACCEPT.", "7. Vòng lặp Reflection Loop: ")
    add_bullet("Đóng gói dữ liệu đạt chuẩn, gửi về cho Chatbot UI hiển thị cho người dùng.", "8. Response Agent: ")

    add_h3("C. Kiểm thử đơn vị, kiểm thử tích hợp & Báo cáo Benchmark định lượng")
    add_bullet(
        "Toàn bộ hệ thống Multi-Agent được kiểm thử tự động tại agent_service/tests/test_multi_agent.py bằng Pytest: Kiểm thử truyền thông điệp Message Bus, kiểm thử Analyst trích xuất giá 'dưới 500k', kiểm thử Critic duyệt ACCEPT và bắt lỗi REVISE, kiểm thử ChromaDB nạp đủ 50 vector sản phẩm, và kiểm thử end-to-end Orchestrator.",
        "Kiểm thử tự động (Unit & Integration Test): "
    )
    add_bullet(
        "Nhóm đã thực hiện bài đo kiểm định lượng giữa Single-Agent (LLM thuần) và Multi-Agent ZShop trên 5 kịch bản tại agent_service/evaluation/BENCHMARK_REPORT.md:\n"
        "- Chống ảo giác (Anti-Hallucination): Single-Agent chỉ đạt 40.0% -> Multi-Agent ZShop đạt 100.0% (+60% độ chính xác).\n"
        "- Tuân thủ ngân sách (Constraint Adherence): Single-Agent 80.0% -> Multi-Agent đạt 100.0%.\n"
        "- Khả năng tự sửa sai (Self-Correction): Single-Agent 0% -> Multi-Agent đạt 100% nhờ Reflection Loop qua Critic Gate.",
        "Báo cáo Benchmark định lượng: "
    )
    add_bullet(
        "Tuyệt đối không hardcode API Key trong mã nguồn. Toàn bộ API Key được lưu trong file .env (đã đưa vào .gitignore) và nạp qua config.py. CSDL sử dụng 100% Parameterized SQL triệt tiêu hoàn toàn nguy cơ SQL Injection. Giao diện React escape dữ liệu chống XSS.",
        "Bảo mật dữ liệu & API Key: "
    )

    # TIÊU CHÍ 4
    add_h2("TIÊU CHÍ 4: SẢN PHẨM, BÁO CÁO VÀ DEMO TRỰC TIẾP (CLO5 - 2.0đ)")
    add_bullet("Giao diện Bento Grid đậm chất Apple, tích hợp không gian 3D tương tác xoay 360 độ, Chatbot UI chia 4 Tab tiện lợi, định dạng tiền tệ formatVND() chuẩn mực không vỡ khung.", "4.1 Giao diện dễ sử dụng (UI/UX): ")
    add_bullet("Có tài liệu README.md chi tiết, hỗ trợ lệnh chạy một bước 'npm run dev:all' (chạy song song Backend 5000 và Frontend 5173). Mã nguồn được quản lý phiên bản bài bản trên Git.", "4.2 Triển khai, README & Git: ")
    add_bullet("Bộ tài liệu kỹ thuật đồ sộ trong thư mục docs/: Tài liệu SRS 97KB, tài liệu kiến trúc UML 2.5, bản thiết kế CSDL 3NF, kế hoạch kiểm thử và báo cáo an ninh mạng.", "4.3 Báo cáo kỹ thuật đầy đủ: ")
    add_bullet(
        "Thực hiện demo trực tiếp trơn tru qua 3 bước không bao giờ xịt:\n"
        "- Bước 1: Mở Chatbot, chat 'Tìm cho tôi củ sạc nhanh dưới 500k' -> Chatbot trả về củ sạc GaN 65W giá 450k; mở log chứng minh Critic vừa duyệt cờ ACCEPT.\n"
        "- Bước 2: Bấm Thêm giỏ hàng -> Trang Checkout -> Chọn thanh toán VietQR Napas 247 -> Hiển thị mã QR và xác nhận thanh toán thành công, hệ thống trừ tồn kho tự động.\n"
        "- Bước 3: Đăng nhập admin@test.com xem Dashboard BI; đăng nhập warehouse@test.com mở AI Stock Copilot xem khuyến nghị nhập các model iPhone sắp cạn kho.",
        "4.4 Kịch bản Demo 3 bước (3 phút ghi điểm tối đa): "
    )

    # TIÊU CHÍ 5
    add_h2("TIÊU CHÍ 5: TƯ DUY PHẢN BIỆN VÀ SỬ DÙNG AI CÓ TRÁCH NHIỆM (CLO1, CLO5 - 2.0đ)")
    add_h3("A. Trả lời câu hỏi: 'AI có bao giờ sinh sai không và em phát hiện, sửa chữa ra sao?'")
    add_body("Khi hội đồng hỏi câu này, hãy tự tin trả lời 3 trường hợp thực tế nhóm đã phát hiện và xử lý:")
    add_bullet(
        "Ban đầu khi prompt thiết kế CSDL, AI tự động sinh ra bảng Sellers (mô hình sàn đa người bán như Shopee). Em đã phản biện rằng ZShop là mô hình Cửa hàng bán lẻ đơn nhất (Single-Store) có kho riêng, việc có bảng Sellers là sai hoàn toàn bản chất bài toán. Em đã loại bỏ bảng này và chuẩn hóa lại thành quy trình Phiếu nhập kho StockImportTickets và bảng Nhân sự Staffs.",
        "1. Phát hiện lỗi Kiến trúc nghiệp vụ: "
    )
    add_bullet(
        "Khi kiểm thử với câu hỏi 'Tìm iPhone dưới 15 triệu', mô hình AI đơn lẻ ban đầu đã tự bịa ra iPhone 15 Pro Max giá 14.500.000đ (thực tế máy có giá trên 28 triệu). Nhóm em đã giải quyết triệt để bằng cách thiết kế Critic Agent độc lập để đối soát với CSDL MySQL và ChromaDB. Nếu giá vượt ngân sách, Critic kích hoạt Reflection Loop ép AI truy xuất lại.",
        "2. Phát hiện lỗi Ảo giác giá (Hallucination): "
    )
    add_bullet(
        "AI thường có xu hướng sinh code nối chuỗi SQL dễ dính lỗ hổng SQL Injection, và sinh định dạng tiền USD hoặc NaN trên giao diện. Em đã rà soát và bắt buộc 100% câu truy vấn phải dùng cú pháp Parameterized SQL, đồng thời viết hàm tiện ích formatVND() để chuẩn hóa tiền tệ Việt Nam.",
        "3. Phát hiện lỗi An ninh & Hiển thị: "
    )
    add_bullet(
        "Nhóm đã chủ động dùng script phân tích tĩnh để rà soát toàn bộ dự án, phát hiện và dọn dẹp triệt để các tàn dư từ miền nghiệp vụ cũ (như số đo vòng 1, vòng 2 trong types.ts, size Freesize trong giỏ hàng, danh mục quần áo trong tài liệu đặc tả), chuẩn hóa 100% sang chuẩn công nghệ Apple ZShop (khổ tay cầm, ưu tiên công thái học 1 tay, củ sạc GaN, MagSafe). Đây là minh chứng rõ nét cho năng lực kiểm soát mã nguồn và tư duy phản biện cao khi ứng dụng AI trong kỹ nghệ phần mềm.",
        "4. Phát hiện và Dọn dẹp Tàn dư Nghiệp vụ (Domain Adaptation): "
    )

    add_h3("B. Phân công vai trò độc lập của 2 thành viên")
    add_bullet(
        "Phụ trách toàn bộ Backend Node.js Express, thiết kế CSDL Microsoft SQL Server 3NF, Cổng thanh toán SZ-Payment, Hệ thống AI Multi-Agent Python (Flask, ChromaDB, Message Bus, Critic Gate), và xây dựng kịch bản kiểm thử Benchmark đánh giá định lượng.",
        "Trưởng nhóm - Nguyễn Quốc Khánh (MSSV: DTC245220042): "
    )
    add_bullet(
        "Phụ trách Frontend React 19 (Showroom 3D iPhone, Bento Grid, ChatBot UI 4 Tab), xây dựng giao diện phân quyền 4 tác nhân (Admin Dashboard, CSKH/POS Portal, Warehouse Portal), Giỏ hàng thông minh và quy trình Đổi trả kèm Thu hồi điểm tích lũy VIP.",
        "Thành viên - Mẫn Bá Hảo: "
    )

    # =========================================================================
    # PHẦN III: BÍ QUYẾT DIỄN TẬP PHÒNG THI & KỸ NĂNG VẤN ĐÁP
    # =========================================================================
    add_h1("PHẦN III: BÍ QUYẾT DIỄN TẬP PHÒNG THI & KỸ NĂNG VẤN ĐÁP")

    add_h2("1. Phím tắt tra cứu nhanh trên VS Code (Mở code trước mặt thầy cô trong 3 giây)")
    add_bullet("Gõ 'critic' -> Nhảy thẳng đến agent_service/agents/critic_agent.py (Chứng minh rào chắn an toàn).", "Ctrl + P: ")
    add_bullet("Gõ 'orchestrator' -> Nhảy thẳng đến agent_service/agents/orchestrator.py (Chứng minh Multi-Agent Bus).", "Ctrl + P: ")
    add_bullet("Gõ 'BENCHMARK' -> Nhảy đến agent_service/evaluation/BENCHMARK_REPORT.md (Chứng minh số liệu định lượng 100% chống ảo giác).", "Ctrl + P: ")
    add_bullet("Gõ 'database.sql' -> Nhảy đến szshop-backend/database.sql (Chứng minh CSDL 11 bảng chuẩn 3NF).", "Ctrl + P: ")
    add_bullet("Gõ 'aiSkills' -> Nhảy đến aiSkills.ts (Chứng minh 13 kỹ năng AI trên giao diện).", "Ctrl + P: ")

    add_h2("2. Top 4 câu hỏi 'bẫy' kinh điển của Hội đồng & Câu trả lời đạt điểm tuyệt đối")
    
    add_h3("Câu 1: 'Hệ thống của em có bị ảo giác giá (Hallucination) không? Làm sao em dám chắc 100%?'")
    add_body(
        "Trả lời: 'Dạ thưa thầy/cô, hệ thống ZShop giải quyết triệt để vấn đề ảo giác giá nhờ kiến trúc Multi-Agent kết hợp Reflection Pattern. "
        "Mô hình không để LLM tự do sinh giá mà có Critic Agent hoạt động độc lập như một cổng gác an toàn. "
        "Critic Agent đối soát sản phẩm được đề xuất với dữ liệu giá thật trong CSDL MySQL và Vector DB ChromaDB. "
        "Nếu sản phẩm vượt trần ngân sách hoặc không có thật, Critic Agent chặn lại và kích hoạt Reflection Loop ép Reasoning Agent truy xuất lại. "
        "Nhóm em đã đo kiểm thực nghiệm qua bài Benchmark, độ chống ảo giác đạt 100% so với 40% của mô hình LLM đơn lẻ ạ.' (Bấm Ctrl+P mở file BENCHMARK_REPORT.md)."
    )

    add_h3("Câu 2: 'Tại sao em không dùng một model LLM duy nhất cho nhanh mà phải chia thành 8 Agent phức tạp?'")
    add_body(
        "Trả lời: 'Dạ thưa thầy/cô, việc sử dụng Single LLM sẽ gặp hiện tượng quá tải nhận thức (Cognitive Overload): Vừa phải bóc tách thực thể, vừa truy vấn dữ liệu, vừa xếp hạng sản phẩm, vừa tự kiểm tra và sinh câu trả lời dẫn đến tỷ lệ ảo giác rất cao (lên tới 60%). "
        "Bằng cách chia thành 8 Agent chuyên biệt qua Message Bus theo nguyên lý đơn nhiệm (Single Responsibility), mỗi Agent chỉ tập trung làm tốt một việc: Analyst bóc tách ý định, Database/RAG truy xuất tri thức thật, Recommendation xếp hạng, và Critic kiểm định độc lập. "
        "Kiến trúc này giúp hệ thống module hóa, dễ dàng viết unit test cho từng tác tử và đạt độ chính xác gần như tuyệt đối ạ.'"
    )

    add_h3("Câu 3: 'Nếu server AI Python bị tắt hoặc mất mạng, trang web của em có bị đơ không?'")
    add_body(
        "Trả lời: 'Dạ thưa thầy/cô, hệ thống được thiết kế theo nguyên lý Graceful Degradation với cơ chế 3-Tier Smart Offline Fallback: "
        "Nếu AI Microservice (cổng 5001) gặp sự cố, request sẽ tự động fallback sang tầng Backend Node.js Express (cổng 5000). "
        "Nếu cả Backend bị ngắt kết nối, ngay tại Frontend (aiSkills.ts) đã tích hợp sẵn một In-Browser Rule Engine xử lý câu hỏi dựa trên danh mục lưu trong bộ nhớ. "
        "Do đó, người dùng luôn nhận được phản hồi và không bao giờ gặp màn hình trắng hay lỗi sập trang ạ.'"
    )

    add_h3("Câu 4: 'CSDL của em đã chuẩn hóa đến mức nào? Có bị dư thừa dữ liệu không?'")
    add_body(
        "Trả lời: 'Dạ thưa thầy/cô, CSDL ZShop gồm 11 bảng chính được chuẩn hóa đạt chuẩn 3NF (Third Normal Form): "
        "Mọi thuộc tính không khóa đều phụ thuộc trực tiếp vào khóa chính, không có phụ thuộc bắc cầu. "
        "Hệ thống phân tách rõ bảng Users (chứa thông tin đăng nhập chung) với bảng Customers (chứa điểm tích lũy VIP) và bảng Staffs (chứa ca làm việc và mã nhân viên). "
        "Các bảng quan hệ nhiều-nhiều như Orders - Products được phân rã qua bảng trung gian OrderItems có lưu trữ unit_price tại thời điểm mua để đảm bảo tính toàn vẹn lịch sử giao dịch ạ.'"
    )

    # Lưu file Word
    doc.save(output_path)
    print(f"Da tao thanh cong tai lieu Word tai: {output_path}")

if __name__ == "__main__":
    out_dir = r"c:\Users\Nguye\OneDrive\Desktop\Project_Ai\_Web_ZShop-main\_Web_ZShop-main"
    main_file = os.path.join(out_dir, "CAM_NANG_VAN_DAP_THI_AI.docx")
    build_docx(main_file)

    # Copy ra Desktop và thư mục E:\Tiêu chí AI nếu có
    try:
        desktop_file = r"C:\Users\Nguye\OneDrive\Desktop\CAM_NANG_VAN_DAP_THI_AI.docx"
        shutil.copyfile(main_file, desktop_file)
        print(f"Da copy sang Desktop: {desktop_file}")
    except Exception as e:
        print(f"Loi copy sang Desktop: {e}")

    try:
        e_dir = r"E:\Tiêu chí AI"
        if not os.path.exists(e_dir):
            # Thử tìm theo wildcards nếu tên thư mục có encoding đặc biệt
            for item in os.listdir("E:\\"):
                if "ti" in item.lower() and "ai" in item.lower():
                    e_dir = os.path.join("E:\\", item)
                    break
        e_file = os.path.join(e_dir, "CAM_NANG_VAN_DAP_THI_AI.docx")
        shutil.copyfile(main_file, e_file)
        print(f"Da copy sang thu muc Tieu chi AI tren o E: {e_file}")
    except Exception as e:
        print(f"Loi copy sang o E: {e}")

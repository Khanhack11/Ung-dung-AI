# Luồng Dữ liệu Chatbot (Chatbot Data Flow)

```mermaid
sequenceDiagram
    autonumber
    actor User as Khách hàng
    participant UI as ChatBot Component
    participant Controller as ChatController (/api/chat)
    participant Engine as AISkillEngine / AiService
    participant Repo as ProductRepository
    participant DB as SQL Server / ChromaDB

    User->>UI: Gửi câu hỏi ("tìm iPhone dưới 15 triệu")
    UI->>Controller: POST /api/chat { text: "tìm iPhone dưới 15 triệu" }
    Controller->>Engine: processChat(text, mode)
    Engine->>Engine: extractPriceRange() -> maxPrice: 15000000
    Engine->>Engine: extractKeywords() -> ['iphone']
    Engine->>Repo: getAllProducts() / search
    Repo->>DB: SELECT * FROM Products WHERE price <= 15000000
    DB-->>Repo: Danh sách sản phẩm iPhone phù hợp
    Repo-->>Engine: Raw Products List
    Engine->>Engine: Lọc: price <= 15000000 && name contains 'iPhone'
    Engine-->>Controller: AISkillResult (message, products)
    Controller-->>UI: JSON { text, skillResult }
    UI-->>User: Hiển thị lời thoại AI & Product Cards
```

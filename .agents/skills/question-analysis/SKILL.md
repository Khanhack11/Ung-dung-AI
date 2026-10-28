---
name: question-analysis
description: Analyze natural language user queries for product search and extract structured intent, entities, and search filters.
---

# Question Analysis Skill

## Objective
Parse natural language queries into structured intent representations for search and retrieval modules without hallucination.

## Input
Natural language question (Vietnamese or English).
Examples:
- *"Có áo hoodie hoặc polo nam dưới 500k không?"*
- *"Tìm giày sneaker size 41 giá từ 500k đến 1 triệu"*
- *"Sản phẩm nào có thời gian bảo hành ít nhất 24 tháng?"*

## Output
Structured intent JSON:
```json
{
  "category": "Phụ kiện sạc & bảo vệ",
  "brands": ["Apple"],
  "min_price": 0,
  "max_price": 500000,
  "min_warranty": 12,
  "size": "65W",
  "sort_by": "price",
  "sort_order": "ASC",
  "keywords": ["củ sạc nhanh", "gan 65w"]
}
```

## Extraction Rules
- **Category Extraction**: Match categories present in the system (`iPhone Flagship`, `iPhone Tiêu chuẩn & Plus`, `iPhone Cổ điển Sưu tầm`, `Phụ kiện sạc & bảo vệ`, `Âm thanh & Tai nghe`).
- **Brand Extraction**: Do NOT invent brands that do not appear in the user's question.
- **Price Normalization**: Normalize price units to standard VND numbers:
  - "dưới 500k" / "dưới 500 nghìn" -> `max_price: 500000`
  - "từ 200k đến 600k" -> `min_price: 200000, max_price: 600000`
  - "tầm 1 triệu" -> `min_price: 700000, max_price: 1300000`
- **Warranty Normalization**: Convert years to months ("ít nhất 2 năm" -> `min_warranty: 24`).
- **Safety**: Do not execute external LLM calls or DB queries directly inside this skill; produce structured intent only.

## Outputs
- `docs/question-analysis.md`
- Intent extraction logic in `aiSkills.ts` / `szshop-backend/services/AiService.js`

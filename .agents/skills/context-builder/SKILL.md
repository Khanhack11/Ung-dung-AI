---
name: context-builder
description: Construct compact, grounded, and relevant textual context from retrieved product records for LLM consumption.
---

# Context Builder Skill

## Objective
Transform database retrieval records into a clean, concise, grounded context string to minimize token consumption and prevent hallucination.

## Input
Array of retrieved product records from `Product Retrieval Skill`.

## Processing Steps
1. **Filter relevant fields**: Extract only essential information needed for recommendation (name, category, price, stock, key specs).
2. **Format Clean Text**: Format each item into standard markdown bullet points.
3. **Format Currency**: Display prices in readable format with thousand separators (e.g. `420.000 VNĐ`).
4. **Enforce Token Budget**: Truncate long descriptions to under 120 characters per item; cap total products in context to maximum 5-8 items.
5. **Handle Empty Results**: If the product array is empty, output an explicit indicator: `KHÔNG TÌM THẤY SẢN PHẨM PHÙ HỢP TRONG CƠ SỞ DỮ LIỆU`.

## Strict Grounding Rules
- **NEVER** add attributes, features, or accessories not present in the database results.
- **NEVER** modify prices, categories, or product names.
- Do NOT generate chatbot conversational text inside this skill; output factual context only.

## Output Format
```text
DANH SÁCH SẢN PHẨM PHÙ HỢP TỪ CSDL (Tổng: 2 sản phẩm):
1. [ID: 1] iPhone 16 Pro Max 256GB Titan Sa Mạc - Giá: 34.990.000 VNĐ | Danh mục: iPhone Flagship | Tồn kho: 45
2. [ID: 25] Củ Sạc Nhanh Apple GaN 65W Ba Cổng Type-C - Giá: 450.000 VNĐ | Danh mục: Phụ kiện sạc & bảo vệ | Tồn kho: 120
```

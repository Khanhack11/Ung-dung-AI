# -*- coding: utf-8 -*-
import os
import re

PATTERNS = [
    r"thời trang", r"thoi trang", r"fashion",
    r"vóc dáng", r"voc dang", r"vòng 1", r"vòng 2", r"vòng 3",
    r"chiều cao", r"cân nặng", r"AI_FASHION_STYLIST", r"AI_SMART_FITTING",
    r"FASHION_OUTFIT", r"outfit", r"phối đồ", r"phoi do", r"lookbook",
    r"áo sơ mi", r"váy", r"đầm", r"chân váy", r"size áo", r"size quần",
    r"quần jean", r"quần tây", r"may đo"
]

REGEX = re.compile("|".join(PATTERNS), re.IGNORECASE)
EXCLUDE_DIRS = {"node_modules", "dist", ".git", ".vscode", "tmp", "__pycache__"}

file_map = {}

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for file in files:
        if file.endswith((".ts", ".tsx", ".js", ".py", ".sql", ".json", ".md")):
            if file in ("scan_fashion.py", "benchmark_results.json"):
                continue
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, 1):
                        match = REGEX.search(line)
                        if match:
                            if path not in file_map:
                                file_map[path] = []
                            file_map[path].append({
                                "line": line_num,
                                "matched": match.group(0),
                                "content": line.strip()
                            })
            except Exception as e:
                pass

with open("scan_report.txt", "w", encoding="utf-8") as out:
    out.write(f"=== TỔNG HỢP {sum(len(v) for v in file_map.values())} ĐIỂM CÒN DƯ THỪA TỪ THỜI TRANG ===\n\n")
    for fpath, items in sorted(file_map.items(), key=lambda x: len(x[1]), reverse=True):
        out.write(f"FILE: {fpath} ({len(items)} điểm)\n")
        for item in items:
            out.write(f"  Line {item['line']}: [{item['matched']}] -> {item['content'][:120]}\n")
        out.write("\n")

print(f"Báo cáo đã ghi vào scan_report.txt với {len(file_map)} files bị ảnh hưởng.")

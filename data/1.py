import json

input_path = r'D:\grad\GradSafe\data\test.json'       # 原始文件路径
output_path = r'D:\grad\GradSafe\data\test_clean.json'  # 输出文件路径

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 只保留 content → user_input, label → toxicity
cleaned_data = [
    {
        "user_input": item["content"],
        "toxicity": item["label"]
    }
    for item in data
    if "content" in item and "label" in item
]

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

print(f"✅ 清洗完成，共保留 {len(cleaned_data)} 条样本。输出文件: {output_path}")

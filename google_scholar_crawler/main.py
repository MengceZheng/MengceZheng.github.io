from scholarly import scholarly
import json
import os
from datetime import datetime

# 获取 Google Scholar ID 并查询作者信息
GOOGLE_SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']
author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)

# 仅填充 'indices' 部分，包含 'citedby' 信息
scholarly.fill(author, sections=['indices'])

# 记录更新时间
author['updated'] = str(datetime.now())

# 打印 JSON 结果，方便调试
print(json.dumps(author, indent=2, ensure_ascii=False))

# 创建结果目录
os.makedirs('results', exist_ok=True)

# 保存数据（仅包含 'indices' 部分）
with open('results/gs_data.json', "w", encoding="utf-8") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

# 生成 shields.io 兼容的 JSON 数据（用于展示引用次数）
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(author.get('citedby', 0)),  # 处理可能缺少 'citedby' 键的情况
}

# 保存 shields.io 统计数据
with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
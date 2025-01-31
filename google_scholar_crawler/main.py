from scholarly import scholarly
import json
import os
from datetime import datetime

# 获取 Google Scholar ID 并查询作者信息
GOOGLE_SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']
author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)

# 填充作者的基本信息、引用指数、统计数据和出版物信息
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

# 记录更新时间
author['updated'] = str(datetime.now())

# 将出版物转换为字典格式（使用 author_pub_id 作为键）
author['publications'] = {pub['author_pub_id']: pub for pub in author['publications']}

# 打印 JSON 结果，方便调试
print(json.dumps(author, indent=2, ensure_ascii=False))

# 创建结果目录
os.makedirs('results', exist_ok=True)

# 获取当前日期
current_date = datetime.now().strftime("%Y-%m-%d")

# 生成带日期的文件名
filename = f"results/gs_data_{current_date}.json"

# 保存完整数据
with open(filename, "w", encoding="utf-8") as outfile:
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

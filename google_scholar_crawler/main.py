import json
import os
import sys
import time
import random
from datetime import datetime

import requests

RESULTS_DIR = 'results'
DATA_FILE = os.path.join(RESULTS_DIR, 'gs_data.json')
SHIELDS_FILE = os.path.join(RESULTS_DIR, 'gs_data_shieldsio.json')

GOOGLE_SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']
SERPAPI_KEY = os.environ.get('SERPAPI_KEY')  # 可选：免费额度 100 次/月，稳定绕过限流

# 兜底默认值（仅在首次运行且所有抓取方式均失败时写入，避免 workflow 红叉）
FALLBACK = {
    "container_type": "Author",
    "filled": ["basics", "indices"],
    "scholar_id": GOOGLE_SCHOLAR_ID,
    "source": "FALLBACK",
    "name": "Mengce Zheng",
    "citedby": 304,
    "citedby5y": 285,
    "hindex": 10,
    "hindex5y": 9,
    "i10index": 10,
    "i10index5y": 9,
}


def load_cached():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None
    return None


def _to_int(val):
    """把 SerpAPI 返回的各种形态（数字/带逗号字符串/嵌套 dict）转成 int。"""
    try:
        if isinstance(val, dict):
            # 如 {"all": "304", "last_5_years": "285"}
            v = val.get('all', val.get('last_5_years', 0))
            return _to_int(v)
        if val is None:
            return 0
        return int(str(val).replace(',', '').strip() or 0)
    except Exception:
        return 0


def fetch_via_serpapi(author_id):
    """通过 SerpAPI 获取 Google Scholar 作者画像（含引用数据）。"""
    resp = requests.get(
        'https://serpapi.com/search.json',
        params={
            'engine': 'google_scholar_author',
            'author_id': author_id,
            'api_key': SERPAPI_KEY,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if 'error' in data:
        raise RuntimeError(f"SerpAPI: {data['error']}")
    # 调试：把原始返回落盘，便于核对字段结构
    try:
        with open(os.path.join(RESULTS_DIR, 'gs_debug_raw.json'), 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
    except Exception:
        pass
    # SerpAPI 返回结构：author 含基础信息；引用指标在顶层 cited_by 对象中
    author = data.get('author', {}) or {}

    cited_by_obj = data.get('cited_by') or author.get('cited_by') or {}
    if isinstance(cited_by_obj, dict):
        # 标准结构：cited_by.table 是多行，每行一个指标（citations / h_index / i10_index）
        table = cited_by_obj.get('table') or []
        # 归并所有行的指标
        merged = {}
        for r in table:
            if isinstance(r, dict):
                merged.update(r)
        if not merged:
            merged = cited_by_obj  # 个别版本直接在顶层
    elif isinstance(cited_by_obj, (int, float, str)):
        merged = {'citations': {'all': cited_by_obj}}
    else:
        merged = {}

    citations = merged.get('citations') or {}
    h_index = merged.get('h_index') or {}
    i10_index = merged.get('i10_index') or {}

    def _pair(v):
        if isinstance(v, dict):
            # 兼容多种“近 5 年”字段命名
            five = (v.get('last_5_years') or v.get('last_five_years')
                    or v.get('since_2021') or v.get('5y') or v.get('5_year')
                    or v.get('last5years'))
            return v.get('all'), five
        return v, None

    c_all, c_5y = _pair(citations)
    h_all, h_5y = _pair(h_index)
    i10_all, i10_5y = _pair(i10_index)

    return {
        'container_type': 'Author',
        'filled': ['basics', 'indices'],
        'scholar_id': author_id,
        'source': 'SERPAPI',
        'name': author.get('name'),
        'affiliation': author.get('affiliations'),
        'interests': [i.get('title') for i in author.get('interests', []) if isinstance(i, dict)],
        'citedby': _to_int(c_all),
        'citedby5y': _to_int(c_5y),
        'hindex': _to_int(h_all),
        'hindex5y': _to_int(h_5y),
        'i10index': _to_int(i10_all),
        'i10index5y': _to_int(i10_5y),
    }


def fetch_via_scholarly(author_id):
    """回退方案：使用 scholarly 直连（CI 固定 IP 易被限流）。"""
    from scholarly import scholarly
    try:
        scholarly.set_timeout(20)
    except Exception:
        pass
    author = scholarly.search_author_id(author_id)
    scholarly.fill(author, sections=['indices'])
    author['source'] = 'SCHOLARLY'
    return author


def fetch_with_fallback(author_id, max_attempts=6, base_wait=20):
    # 首选 SerpAPI（若有 key）
    if SERPAPI_KEY:
        try:
            return fetch_via_serpapi(author_id)
        except Exception as e:
            print(f"[WARN] SerpAPI 失败，回退 scholarly: {e}", file=sys.stderr)

    # 回退 scholarly 直连，带指数退避
    last_err = None
    for attempt in range(1, max_attempts + 1):
        try:
            return fetch_via_scholarly(author_id)
        except Exception as e:
            last_err = e
            print(f"[WARN] scholarly attempt {attempt}/{max_attempts} failed: {e}", file=sys.stderr)
            if attempt < max_attempts:
                sleep_for = base_wait * (2 ** (attempt - 1)) + random.uniform(0, 10)
                print(f"[INFO] 等待 {sleep_for:.1f}s 后重试...", file=sys.stderr)
                time.sleep(sleep_for)
    raise last_err


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    cached = load_cached()

    # 随机预热，错峰（10 秒内）
    jitter = random.uniform(0, 10)
    print(f"[INFO] 随机预热等待 {jitter:.1f}s...", file=sys.stderr)
    time.sleep(jitter)

    try:
        author = fetch_with_fallback(GOOGLE_SCHOLAR_ID)
    except Exception as e:
        print(f"[ERROR] 无法获取数据: {e}", file=sys.stderr)
        if cached is not None:
            print("[INFO] 回退到上次成功抓取的结果。", file=sys.stderr)
            author = cached
        else:
            print("[WARN] 无缓存，写入兜底默认值（引用数可能滞后）。", file=sys.stderr)
            author = dict(FALLBACK)

    author['updated'] = str(datetime.now())
    print(json.dumps(author, indent=2, ensure_ascii=False))

    with open(DATA_FILE, "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author.get('citedby', 0)),
    }
    with open(SHIELDS_FILE, 'w', encoding='utf-8') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)


if __name__ == '__main__':
    main()

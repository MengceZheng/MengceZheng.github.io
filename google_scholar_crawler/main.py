import logging
from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os

logging.basicConfig(level=logging.INFO)

try:
    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg)

    author = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']: v for v in author['publications']}

    os.makedirs('results', exist_ok=True)
    with open('results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author.get('citedby', 0)}",
    }
    with open('results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)

except Exception as e:
    logging.error(f"An error occurred: {e}")

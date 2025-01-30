import os
import json
import time
from datetime import datetime
from functools import wraps
from typing import Dict, Any

from scholarly import scholarly
from tenacity import retry, stop_after_attempt, wait_exponential

def retry_on_error(func):
    @wraps(func)
    @retry(stop=stop_after_attempt(int(os.getenv('MAX_RETRIES', 3))),
           wait=wait_exponential(multiplier=1, min=4, max=10))
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper

@retry_on_error
def fetch_author_data(author_id: str) -> Dict[str, Any]:
    author = scholarly.search_author_id(author_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    return author

def process_publications(publications: list) -> Dict[str, Any]:
    return {
        pub['author_pub_id']: {
            'title': pub.get('bib', {}).get('title'),
            'year': pub.get('bib', {}).get('pub_year'),
            'citations': pub.get('num_citations', 0),
            'venue': pub.get('bib', {}).get('citation')
        }
        for pub in publications
    }

def save_data(data: Dict[str, Any], filename: str) -> None:
    temp_file = f"{filename}.tmp"
    with open(temp_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(temp_file, filename)

def main():
    output_dir = os.path.join('results', datetime.now().strftime('%Y/%m'))
    os.makedirs(output_dir, exist_ok=True)

    author = fetch_author_data(os.environ['GOOGLE_SCHOLAR_ID'])
    
    processed = {
        'metadata': {
            'updated': datetime.now().isoformat(),
            'scholar_id': os.environ['GOOGLE_SCHOLAR_ID'],
            'name': author.get('name')
        },
        'stats': {
            'citations': author.get('citedby', 0),
            'hindex': author.get('hindex', 0),
            'i10index': author.get('i10index', 0)
        },
        'publications': process_publications(author.get('publications', []))
    }

    save_data(processed, os.path.join(output_dir, f"scholar_{datetime.now().strftime('%Y%m%d')}.json"))

    shield_data = {
        "schemaVersion": 1,
        "label": "Citations",
        "message": f"{processed['stats']['citations']}",
        "color": "brightgreen",
        "cacheSeconds": 43200
    }
    save_data(shield_data, os.path.join(output_dir, 'badge_data.json'))

if __name__ == "__main__":
    main()
from elasticsearch import Elasticsearch
import json
from tqdm import tqdm

# Load documents
with open("documents.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

# Connect to local Elasticsearch
es = Elasticsearch("http://localhost:9200")
index_name = "course_questions"

# Define index config
index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"}
        }
    }
}

# Safely delete index if it exists
if es.indices.exists(index=index_name):  # or use request={"index": index_name} if needed
    es.indices.delete(index=index_name)

# Create index
es.indices.create(index=index_name, body=index_settings)

# Index documents
for doc in tqdm(documents):
    es.index(index=index_name, document=doc)

print("✅ Indexing complete.")

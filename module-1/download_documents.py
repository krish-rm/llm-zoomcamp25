# download_documents.py

import requests
import json

docs_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main/01-intro/documents.json?raw=1'
docs_response = requests.get(docs_url)
documents_raw = docs_response.json()

documents = []

for course in documents_raw:
    course_name = course['course']
    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)

# Save it locally so you can use it later
with open("documents.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=2, ensure_ascii=False)

print(f"✅ Downloaded and saved {len(documents)} documents to documents.json")

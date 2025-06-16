from elasticsearch import Elasticsearch
import json

es_client = Elasticsearch("http://localhost:9200")

query = "How do copy a file to a Docker container?"

search_query = {
    "size": 3,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^4", "text"],
                    "type": "best_fields"
                }
            },
            "filter": {
                "term": {
                    "course": "machine-learning-zoomcamp"
                }
            }
        }
    }
}

response = es_client.search(index="course_questions", body=search_query)

# Print top 3 results
for idx, hit in enumerate(response["hits"]["hits"], start=1):
    print(f"{idx}. {hit['_source']['question']} (score: {round(hit['_score'], 2)})")

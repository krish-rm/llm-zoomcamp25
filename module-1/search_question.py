from elasticsearch import Elasticsearch
import json

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")
index_name = "course_questions"

query = "How do execute a command on a Kubernetes pod?"

# Build search query
search_body = {
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^4", "text"],
                    "type": "best_fields"
                }
            }
        }
    }
}

# Run the search
response = es.search(index=index_name, body=search_body)

# Print top result and score
top_hit = response["hits"]["hits"][0]
print("Question:", top_hit["_source"]["question"])
print("Score:", round(top_hit["_score"], 2))

# for hit in response["hits"]["hits"]:
#     score = round(hit["_score"], 2)
#     question = hit["_source"]["question"]
#     text = hit["_source"]["text"]
#     section = hit["_source"]["section"]
#     course = hit["_source"]["course"]

#     print(f"🟩 Score: {score}")
#     print(f"📘 Course: {course}")
#     print(f"📌 Section: {section}")
#     print(f"❓ Question: {question}")
#     print(f"📝 Answer: {text}")
#     print("-" * 100)

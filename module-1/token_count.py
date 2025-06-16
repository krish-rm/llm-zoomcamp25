from elasticsearch import Elasticsearch
from pprint import pprint
import tiktoken

# Connect to local Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Define the query
query = {
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": "How do copy a file to a Docker container?",
                        "fields": ["question^4", "text"],
                        "type": "best_fields"
                    }
                }
            ],
            "filter": [
                {"term": {"course": "machine-learning-zoomcamp"}}
            ]
        }
    }
}

# Perform the search
response = es.search(index="course_questions", query=query["query"], size=3)

# Extract relevant fields
results = []
for hit in response["hits"]["hits"]:
    source = hit["_source"]
    results.append({
        "question": source["question"],
        "text": source["text"]
    })

# Context template
context_template = """
Q: {question}
A: {text}
""".strip()

# Format context
context_entries = [
    context_template.format(question=doc["question"], text=doc["text"])
    for doc in results
]
context = "\n\n".join(context_entries)

# Prompt template
prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()

# Build final prompt
final_prompt = prompt_template.format(
    question="How do copy a file to a Docker container?",
    context=context
)

# Print prompt (optional)
print(final_prompt)

# Calculate token count using tiktoken
encoding = tiktoken.encoding_for_model("gpt-4o")
tokens = encoding.encode(final_prompt)
print("\n\nToken count:", len(tokens))

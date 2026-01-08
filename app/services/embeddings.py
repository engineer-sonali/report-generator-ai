from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from uuid import uuid4
import os

# Local embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Persistent Qdrant storage
QDRANT_PATH = "./qdrant_data"
os.makedirs(QDRANT_PATH, exist_ok=True)

qdrant = QdrantClient(path=QDRANT_PATH)

COLLECTION = "documents"

# Create collection ONLY if it doesn't exist
existing = [c.name for c in qdrant.get_collections().collections]

if COLLECTION not in existing:
    qdrant.create_collection(
        collection_name=COLLECTION,
        vectors_config={
            "size": 384,
            "distance": "Cosine"
        }
    )

def embed_and_store(text: str) -> str:
    embedding = model.encode(text).tolist()
    vector_id = str(uuid4())

    point = PointStruct(
        id=vector_id,
        vector=embedding,
        payload={"text": text}
    )

    qdrant.upsert(
        collection_name=COLLECTION,
        points=[point]
    )

    return vector_id


def search_similar(query: str, limit: int = 5):
    query_embedding = model.encode(query).tolist()

    return qdrant.search(
        collection_name=COLLECTION,
        query_vector=query_embedding,
        limit=limit
    )

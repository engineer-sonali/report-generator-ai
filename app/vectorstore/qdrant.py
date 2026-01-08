from app.services.embeddings import client

def fetch_all_embeddings() -> str:
    records = client.scroll(
        collection_name="documents",
        limit=50
    )[0]

    texts = []
    for r in records:
        texts.append(r.payload.get("text", ""))

    return "\n".join(texts)

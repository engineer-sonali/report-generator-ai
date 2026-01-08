from app.services.local_storage import upload_file
from app.services.embeddings import embed_and_store
from app.db.session import SessionLocal
from app.db.models import UploadedFile

def ingest_file(file):
    db = SessionLocal()

    file_path = upload_file(file.file, file.filename)

    vector_id = embed_and_store(file.filename)

    db_file = UploadedFile(
        filename=file.filename,
        file_type=file.content_type,
        file_path=file_path
    )

    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return {
        "file_id": db_file.id,
        "filename": db_file.filename,
        "vector_id": vector_id
    }

# app/services/s3_service.py
import boto3

s3 = boto3.client("s3")

def upload_to_s3(file, bucket):
    s3.upload_fileobj(file, bucket, file.filename)
    return f"s3://{bucket}/{file.filename}"

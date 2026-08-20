from pathlib import Path
from minio import Minio

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin123",
    secure=False
)

bucket_name = "images"

def upload_image(file_path):
    file = Path(file_path)

    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    client.fput_object(
        bucket_name,
        file.name,
        str(file)
    )

    print("Upload thành công:", file.name)


upload_image("photo.jpg")
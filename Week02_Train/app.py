from pathlib import Path
from minio import Minio
from minio.error import S3Error

client = Minio(
    "localhost:9000",
    access_key="Admin",
    secret_key="Admin@123",
    secure=False
)

bucket_name = "images"


def upload_image(file_path: str) -> bool:
    file = Path(file_path)

    try:
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)

        client.fput_object(
            bucket_name,
            file.name,
            str(file)
        )
        print("Upload thành công:", file.name)
        return True

    except S3Error as e:
        print("Lỗi khi upload:", e)
        return False
    except FileNotFoundError:
        print("Không tìm thấy file:", file_path)
        return False


def download_image(object_name: str, save_path: str) -> bool:
    try:
        client.fget_object(
            bucket_name=bucket_name,
            object_name=object_name,
            file_path=save_path,
        )
        print(f"Download thành công: {bucket_name}/{object_name} -> {save_path}")
        return True

    except S3Error as e:
        print(f"Lỗi khi download: {e}")
        return False


if __name__ == "__main__":
    upload_image("D:/intern-thien/intern-training/Week02_Train/test.jpg")

    download_image(
        object_name="test.jpg",
        save_path="D:/intern-thien/intern-training/Week02_Train/image/test.jpg",
    )

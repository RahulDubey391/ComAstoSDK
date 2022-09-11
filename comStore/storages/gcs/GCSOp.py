import gcsfs
from google.cloud import storage

class GCSOperator(object):

    def __init__(self):
        self.client = storage.Client()

    def put(self,bucket_name: str,blob_name: str,data: str) -> None:
        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(data)

    def get(self,bucket_name: str,blob_name: str):
        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        return blob

    def list(self,bucket_name: str) -> list:
        bucket = self.client.get_bucket(bucket_name)
        blobs = bucket.list_blobs()
        return blobs

    def move(self,src_path: str, dest_path: str) -> None:
        pass
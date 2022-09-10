import gcsfs
from google.cloud import storage

class GCSOperator(object):

    def __init__(self):
        pass

    def put(self,path: str) -> None:
        pass

    def get(self,path: str) -> None:
        pass

    def list(self,path: str) -> None:
        pass

    def move(self,src_path: str, dest_path: str) -> None:
        pass
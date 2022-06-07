import datetime
import hashlib
import uuid


class provider:
    def __init__(self):
        pass

    def GUID(self):
        return str(uuid.uuid4()).upper()

    def NOW(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def SHA256(self, data):
        return hashlib.sha256(data.encode()).hexdigest().upper()

    def CONCAT_WS(self, joiner, *data):
        return joiner.join(data)

from uuid import uuid4

def get_uuid(documents):
    return [str(uuid4()) for _ in range(len(documents))]
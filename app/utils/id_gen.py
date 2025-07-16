import os, uuid

def gen_unique_id():
    while True:
        paste_id = uuid.uuid4().hex[:8]
        if not os.path.exists(f"../storage/{paste_id}.txt"):
            return paste_id

import uuid
from datetime import datetime

def generate_batch_id():
    return str(uuid.uuid4())

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

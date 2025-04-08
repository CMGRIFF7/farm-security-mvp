import random
import time

def read_rfid_tag():
    sample_tags = ['TAG123', 'TAG456', 'TAG789']
    tag_id = random.choice(sample_tags)
    timestamp = time.time()
    return tag_id, timestamp
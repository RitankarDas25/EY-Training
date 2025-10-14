# producer.py
import json
import time

def producer(q):
    # Simulate a task
    task = {
        "student_id": 101,
        "action": "generate_certificate",
        "email": "ygdybgfbt@yjfd.com"
    }

    print("[Producer] Sending task:", task)
    q.put(json.dumps(task))  # Convert to JSON string for consistency
    time.sleep(1)
    q.put(None)  # Signal to stop
    print("[Producer] Task sent and producer is done.")

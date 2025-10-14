# consumer.py
import json
import time

def consumer(q):
    print("[Consumer] Waiting for tasks...")

    while True:
        message = q.get()

        if message is None:
            print("[Consumer] Received stop signal. Exiting.")
            break

        task = json.loads(message)
        print(f"[Consumer] Received task: {task}")

        # Simulate processing
        time.sleep(2)
        print(f"[Consumer] Processed task for student: {task['student_id']}")

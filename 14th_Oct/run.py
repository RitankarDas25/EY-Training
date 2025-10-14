# run.py
from multiprocessing import Process, Queue
from producer import producer
from consumer import consumer

if __name__ == "__main__":
    q = Queue()

    # Start the consumer process
    consumer_process = Process(target=consumer, args=(q,))
    consumer_process.start()

    # Start the producer process
    producer_process = Process(target=producer, args=(q,))
    producer_process.start()

    producer_process.join()
    consumer_process.join()

    print("[Main] All processes completed.")

import time
import multiprocessing
import math
import threading


def square_root():
    for _ in range(10000000):
        result = math.sqrt(big_number)
    print(f"{big_number} answer: {result}")


def without_anything():
    start = time.time()
    for i in range(5):
        square_root()
    end = time.time() - start
    print(f"without anything {end}")


def with_threads():
    threads = [threading.Thread(target=square_root) for i in range(5)]
    start_time = time.time()
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    end_time = time.time() - start_time
    print(f"It took with threading {end_time} seconds")


if __name__ == '__main__':
    multiprocessing.freeze_support()
    processes = [multiprocessing.Process(target=square_root) for i in range(5)]
    start_time = time.time()
    for p in processes:
        p.start()

    for p in processes:
        p.join()
    end_time = time.time() - start_time
    print(f"It took with multiprocessing {end_time} seconds")  #2.18

without_anything() #6.28
with_threads() #6.45
with_multiprocessing #2.18
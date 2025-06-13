"""
1_basicMultithreading.py
------------------------
This script demonstrates the need for multithreading and the basics of using threads in Python.

Key Concepts:
1. Why use multithreading? (I/O-bound tasks, responsiveness, concurrency)
2. Creating and starting threads using the threading module
3. Comparing sequential vs. multithreaded execution

Scenario:
- Simulate downloading files (I/O-bound task) sequentially and with threads
"""

import threading
import time

def download_file(file_name, delay):
    """
    Simulates downloading a file by sleeping for 'delay' seconds.
    """
    print(f"Starting download: {file_name}")
    time.sleep(delay)
    print(f"Finished download: {file_name}")

if __name__ == "__main__":
    files = [
        ("file1.txt", 2),
        ("file2.txt", 3),
        ("file3.txt", 1)
    ]

    print("Sequential download (no threads):")
    start = time.time()
    for file_name, delay in files:
        download_file(file_name, delay)
    print(f"Total time (sequential): {time.time() - start:.2f} seconds\n")

    print("Multithreaded download:")
    threads = []
    start = time.time()
    for file_name, delay in files:
        t = threading.Thread(target=download_file, args=(file_name, delay))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Total time (multithreaded): {time.time() - start:.2f} seconds\n")

    print("""
Explanation:
- In the sequential approach, each file is downloaded one after another, so the total time is the sum of all delays.
- In the multithreaded approach, downloads happen concurrently, so the total time is close to the longest single delay.
- This demonstrates the benefit of multithreading for I/O-bound tasks.
""")

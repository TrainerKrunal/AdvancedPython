"""
3_sychronization.py
-------------------
This script demonstrates how to avoid race conditions in multithreading using thread synchronization (Lock) in Python.
It uses the same real-time bank account example as in 2_racecondition.py, but with proper locking.

Key Concepts:
1. Using threading.Lock to synchronize access to shared data
2. Preventing race conditions and ensuring data integrity

Explanation:
- A Lock ensures that only one thread can execute a block of code at a time (critical section).
- This prevents multiple threads from modifying shared data simultaneously, avoiding race conditions.
"""

import threading
import time

class BankAccount:
    def __init__(self, acc_holder, initial_balance):
        self.holder = acc_holder
        self.balance = initial_balance
        self.lock = threading.Lock()  # Create a lock for synchronization

    def withdraw(self, amount):
        """
        Thread-safe withdraw method using a lock.
        Only one thread can execute the critical section at a time.
        """
        with self.lock:  # Acquire the lock before accessing/modifying shared data
            if self.balance >= amount:
                time.sleep(0.1)  # Simulate processing delay
                self.balance -= amount
                print(f"{threading.current_thread().name} withdrew {amount}. Remaining balance: {self.balance}")
            else:
                print(f"{threading.current_thread().name} failed to withdraw {amount}. Insufficient funds!")

if __name__ == "__main__":
    acc = BankAccount("Alice", 100)

    def try_withdraw():
        acc.withdraw(80)

    # Create two threads that try to withdraw from the same account
    t1 = threading.Thread(target=try_withdraw, name="Thread-1")
    t2 = threading.Thread(target=try_withdraw, name="Thread-2")

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"Final balance: {acc.balance}")

    print("""
Explanation:
- The with self.lock: statement ensures that only one thread can execute the withdraw logic at a time.
- This prevents both threads from withdrawing simultaneously and causing an overdraw.
- Using locks is essential for thread safety when working with shared data.
""")

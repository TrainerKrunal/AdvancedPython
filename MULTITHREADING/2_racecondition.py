"""
2_racecondition.py
------------------
This script demonstrates a race condition in multithreading using a real-time bank account example.


Key Concepts:
1. What is a race condition?
   - A race condition occurs when two or more threads access shared data at the same time, and the final outcome depends on the order in which the threads execute.
   - This can lead to unpredictable and incorrect results, especially when threads read and write shared variables without proper coordination.

2. How race conditions can occur in shared data scenarios:
   - If multiple threads check and update a shared variable (like a bank account balance) simultaneously, they may both see the same value and proceed, causing logical errors (e.g., overdrawn accounts).
   - This is common in banking, ticket booking, and other real-world systems where resources are shared.

3. Why synchronization (locks) is important:
   - Synchronization mechanisms like threading.Lock ensure that only one thread can access a critical section of code at a time.
   - This prevents race conditions by making sure that shared data is updated safely, preserving data integrity.

Scenario:
- Two threads try to withdraw money from the same bank account at the same time.
- Without synchronization, both may succeed even if the balance is insufficient, leading to incorrect results.
"""

import threading
import time

class BankAccount:
    def __init__(self, acc_holder, initial_balance):
        self.holder = acc_holder
        self.balance = initial_balance

    def withdraw(self, amount):
        """
        Withdraw money if sufficient balance exists.
        This method is NOT thread-safe and can lead to a race condition.
        """
        if self.balance >= amount:
            # Simulate processing delay
            time.sleep(0.1)
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
- Both threads check the balance before withdrawing, but due to the delay, both may see enough balance and proceed.
- This leads to the account being overdrawn, which is a classic race condition.
- In real applications, you must use synchronization (e.g., threading.Lock) to prevent such issues.
""")

"""
2_realtimegenerators.py
-----------------------
This script demonstrates a real-time bank scenario where generators are useful.

Scenario:
- A bank needs to process a large number of transactions (e.g., millions) for auditing or reporting.
- Instead of loading all transactions into memory, a generator yields one transaction at a time, making the process memory efficient and scalable.

Key Concepts:
1. Using generators to process large datasets efficiently
2. Lazy evaluation in real-world applications
"""

import random
import time

def generate_transactions(num_transactions):
    """
    Generator that yields fake bank transactions one by one.
    Each transaction is a dictionary with id, type, and amount.
    """
    for i in range(1, num_transactions + 1):
        txn = {
            'id': i,
            'type': random.choice(['deposit', 'withdrawal']),
            'amount': round(random.uniform(10, 1000), 2)
        }
        yield txn
        # Simulate delay for realism (remove/comment for faster demo)
        # time.sleep(0.001)

if __name__ == "__main__":
    print("Processing first 5 transactions out of 1,000,000 (using a generator):")
    txn_gen = generate_transactions(1_000_000)
    for _ in range(5):
        txn = next(txn_gen)
        print(txn)

    print("\nProcessing all transactions and calculating total deposits:")
    txn_gen = generate_transactions(1_000_000)
    total_deposit = 0
    for txn in txn_gen:
        if txn['type'] == 'deposit':
            total_deposit += txn['amount']
    print(f"Total deposit amount: {total_deposit:.2f}")

    print("""
Explanation:
- The generator yields one transaction at a time, so memory usage stays low even for millions of transactions.
- This is ideal for processing logs, records, or any large data stream in banking and finance.
""")

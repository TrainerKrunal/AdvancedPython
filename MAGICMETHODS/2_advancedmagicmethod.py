"""
2_advancedmagicmethod.py
------------------------
This script demonstrates advanced usage of magic methods (dunder methods) in Python with a real-world example and detailed comments.

Key Concepts:
1. Customizing object behavior with magic methods
2. Implementing __len__, __getitem__, __setitem__, __iter__, and __contains__
3. Making your class behave like a built-in collection

Scenario:
- BankLedger: A class that stores multiple BankAccount objects and behaves like a list/dictionary.
"""

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def __str__(self):
        return f"BankAccount(holder={self.holder}, balance={self.balance})"

class BankLedger:
    """
    BankLedger stores multiple BankAccount objects and supports:
    - len(ledger): number of accounts (__len__)
    - ledger[index]: get account by index (__getitem__)
    - ledger[index] = value: set account at index (__setitem__)
    - for acc in ledger: iterate over accounts (__iter__)
    - acc in ledger: check if account exists (__contains__)
    """
    def __init__(self):
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def __len__(self):
        # Returns the number of accounts
        return len(self._accounts)

    def __getitem__(self, index):
        # Allows access by index (ledger[index])
        return self._accounts[index]

    def __setitem__(self, index, value):
        # Allows setting an account at a specific index
        if not isinstance(value, BankAccount):
            raise ValueError("Value must be a BankAccount object")
        self._accounts[index] = value

    def __iter__(self):
        # Allows iteration over accounts
        return iter(self._accounts)

    def __contains__(self, account):
        # Allows use of 'in' to check if an account exists
        return account in self._accounts

if __name__ == "__main__":
    acc1 = BankAccount("Alice", 1000)
    acc2 = BankAccount("Bob", 1500)
    acc3 = BankAccount("Charlie", 2000)

    ledger = BankLedger()
    ledger.add_account(acc1)
    ledger.add_account(acc2)
    ledger.add_account(acc3)

    print(f"Number of accounts: {len(ledger)}")  # Calls __len__
    print(f"First account: {ledger[0]}")         # Calls __getitem__
    ledger[1] = BankAccount("Bob", 1800)        # Calls __setitem__
    print(f"Updated second account: {ledger[1]}")

    print("All accounts:")
    for acc in ledger:                           # Calls __iter__
        print(acc)

    print(f"Is acc1 in ledger? {acc1 in ledger}")  # Calls __contains__
    print(f"Is BankAccount('Dave', 500) in ledger? {BankAccount('Dave', 500) in ledger}")

    print("""
Explanation:
- __len__ lets you use len() on your object.
- __getitem__ and __setitem__ let you use indexing and assignment.
- __iter__ lets you iterate over your object in a for loop.
- __contains__ lets you use 'in' to check for membership.
- This makes your custom class behave like a built-in collection.
""")

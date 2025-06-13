"""
1_basicmagicmethod.py
---------------------
This script explains the basics of magic methods (dunder methods) in Python with examples and comments.

Key Concepts:
1. What are magic methods?
2. Why do we need magic methods?
3. Commonly used magic methods

What are magic methods?
------------------------
- Magic methods (also called dunder methods) are special methods in Python that start and end with double underscores (e.g., __init__, __str__, __add__).
- They allow you to define how objects of your class behave with built-in operations (like printing, addition, comparison, etc.).

Why do we need magic methods?
-----------------------------
- Magic methods let you customize the behavior of your objects for built-in functions and operators.
- They make your classes more Pythonic and integrate smoothly with the language features.
- Examples: object construction (__init__), string representation (__str__), operator overloading (__add__, __eq__), etc.

Example: BankAccount class with basic magic methods
---------------------------------------------------
"""

class BankAccount:
    def __init__(self, holder, balance):
        # __init__ is the constructor magic method
        self.holder = holder
        self.balance = balance

    def __str__(self):
        # __str__ defines the string representation of the object
        return f"BankAccount(holder={self.holder}, balance={self.balance})"

    def __add__(self, other):
        # __add__ allows using + to combine two BankAccount balances
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        return NotImplemented

    def __eq__(self, other):
        # __eq__ allows using == to compare two BankAccount objects
        if isinstance(other, BankAccount):
            return self.holder == other.holder and self.balance == other.balance
        return False

if __name__ == "__main__":
    acc1 = BankAccount("Alice", 1000)
    acc2 = BankAccount("Bob", 1500)
    acc3 = BankAccount("Alice", 1000)

    print(acc1)  # Calls __str__
    print(acc2)

    print(f"Total balance (acc1 + acc2): {acc1 + acc2}")  # Calls __add__
    print(f"acc1 == acc3? {acc1 == acc3}")  # Calls __eq__
    print(f"acc1 == acc2? {acc1 == acc2}")

    print("""
Explanation:
- __init__ is called when an object is created.
- __str__ is called when printing the object.
- __add__ is called when using + between two BankAccount objects.
- __eq__ is called when using == to compare two BankAccount objects.
- Magic methods make your classes work naturally with Python's built-in features.
""")

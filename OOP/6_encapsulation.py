"""
6_encapsulation.py
------------------
This script demonstrates encapsulation and basic data hiding in Python using double underscores (__).

Key Concepts:
1. Encapsulation: Bundling data and methods that operate on that data within a class.
2. Data Hiding: Using double underscores (__) to make attributes private (name mangling).
3. Accessing and modifying private attributes using methods.

Scenario:
- BankAccount: Demonstrates private balance attribute and controlled access via methods.
"""

class BankAccount:
    def __init__(self, acc_holder, initial_balance):
        self.holder = acc_holder
        self.__balance = initial_balance  # Private attribute (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        """
        Public method to access the private balance attribute.
        """
        return self.__balance

if __name__ == "__main__":
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(f"Current balance (via method): {acc.get_balance()}")

    # Attempt to access the private attribute directly (will fail)
    try:
        print(acc.__balance)
    except AttributeError as e:
        print(f"Error: {e}")

    # Accessing the private attribute using name mangling (not recommended)
    print(f"Accessing hidden balance: {acc._BankAccount__balance}")

    # This demonstrates how double underscores provide basic data hiding in Python.

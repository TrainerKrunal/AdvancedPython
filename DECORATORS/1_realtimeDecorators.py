"""
1_realtimeDecorators.py
-----------------------
This script explains the concept of decorators in Python with a real-time bank scenario.

Key Concepts:
1. What is a decorator?
2. Why do we need decorators?
3. How to use decorators in real-world applications

What is a decorator?
---------------------
- A decorator is a function that takes another function and extends or alters its behavior without explicitly modifying it.
- Decorators are often used for logging, access control, timing, validation, and more.
- In Python, decorators are applied using the @decorator_name syntax above a function definition.

Why do we need decorators?
--------------------------
- Decorators help keep code DRY (Don't Repeat Yourself) by allowing you to reuse common logic across multiple functions.
- They separate cross-cutting concerns (like logging, security, or validation) from business logic, making code cleaner and more maintainable.

Scenario:
- In a bank, certain operations (like withdrawals) may require logging or security checks.
- A decorator can be used to add logging to these operations without changing their core logic.
"""


# Simple decorator for logging bank operations (no functools, no kwargs)
def log_operation(func):
    """
    Decorator that logs the function call and its result.
    Only works for functions with two arguments: self and amount.
    """
    def wrapper(self, amount):
        print(f"[LOG] Calling {func.__name__} with amount={amount}")
        result = func(self, amount)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

class BankAccount:
    def __init__(self, acc_holder, initial_balance):
        self.holder = acc_holder
        self.balance = initial_balance

    @log_operation
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    @log_operation
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

if __name__ == "__main__":
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    acc.withdraw(2000)

    print("""
Explanation:
- The @log_operation decorator adds logging to deposit and withdraw methods.
- This keeps the business logic clean and reusable, while logging is handled separately.
- Decorators are powerful for adding cross-cutting features like logging, security, or validation in real-world applications.
""")

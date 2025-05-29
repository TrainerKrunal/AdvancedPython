"""
5_properydecorators.py
----------------------
This script demonstrates the use of property decorators and custom descriptors in Python
using a real-time bank scenario.

Key Concepts:
1. @property decorator for getter, setter, and deleter
2. Encapsulation and validation using properties
3. Custom descriptor for attribute management

What is the use of property?
---------------------------
- The @property decorator allows you to define methods in a class that can be accessed like attributes.
- It enables encapsulation: you can control access, validation, and logic when getting, setting, or deleting an attribute.
- This makes your class interface cleaner and safer, as users interact with attributes, not explicit getter/setter methods.

What is the use of a custom descriptor?
--------------------------------------
- A custom descriptor is a class that defines any of the methods __get__, __set__, or __delete__.
- Descriptors allow you to manage the behavior of attribute access at a lower level than properties.
- They are reusable and can be shared across multiple classes, providing advanced control over attribute access, validation, and storage.

Scenario:
- BankAccount: Uses property decorators to manage balance with validation
- Customer: Uses a custom descriptor to manage and validate the email attribute
"""

# Property Decorators Example
class BankAccount:
    def __init__(self, acc_holder, initial_balance):
        self.holder = acc_holder
        self._balance = initial_balance  # Private attribute by convention

    @property
    def balance(self):
        """
        Getter for balance. Allows access like an attribute, but can include logic.
        """
        return self._balance

    @balance.setter
    def balance(self, amount):
        """
        Setter for balance. Allows validation before setting the value.
        """
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = amount

    @balance.deleter
    def balance(self):
        """
        Deleter for balance. Allows custom logic when deleting the attribute.
        """
        print("Balance deleted!")
        self._balance = 0

# Custom Descriptor Example
class EmailDescriptor:
    """
    Custom descriptor to manage and validate email attribute.
    Demonstrates __get__, __set__, and __delete__ methods.
    """
    def __init__(self):
        self._email = None

    def __get__(self, instance, owner):
        return self._email

    def __set__(self, instance, value):
        if "@" not in value:
            raise ValueError("Invalid email address!")
        self._email = value

    def __delete__(self, instance):
        print("Email deleted!")
        self._email = None

class Customer:
    email = EmailDescriptor()  # Using the custom descriptor

    def __init__(self, name, email):
        self.name = name
        self.email = email  # Triggers EmailDescriptor.__set__

if __name__ == "__main__":
    # Property Decorator Demo
    acc = BankAccount("Alice", 1000)
    print(f"Initial balance: {acc.balance}")  # Calls getter
    acc.balance = 2000  # Calls setter
    print(f"Updated balance: {acc.balance}")
    try:
        acc.balance = -500  # Should raise ValueError
    except ValueError as e:
        print(e)
    del acc.balance  # Calls deleter
    print(f"Balance after deletion: {acc.balance}")

    print("\n---\n")

    # Custom Descriptor Demo
    cust = Customer("Bob", "bob@example.com")
    print(f"Customer: {cust.name}, Email: {cust.email}")
    try:
        cust.email = "bobexample.com"  # Should raise ValueError
    except ValueError as e:
        print(e)
    del cust.email
    print(f"Email after deletion: {cust.email}")

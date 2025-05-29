"""
4_multipleinheritance.py
-----------------------
This script demonstrates multiple inheritance and Method Resolution Order (MRO) in Python.
A real-time bank scenario is used for clarity.

Key Concepts:
1. Multiple Inheritance
2. Method Resolution Order (MRO)
3. Use of super() in multiple inheritance

Scenario:
- Account: Base class for all accounts
- ATMCard: Class representing ATM card features
- OnlineBanking: Class representing online banking features
- CustomerAccount: Inherits from Account, ATMCard, and OnlineBanking

Explanation of MRO (Method Resolution Order):
------------------------------------------------
MRO is the order in which Python looks for a method or attribute in a hierarchy involving multiple inheritance.
It determines which class's method is called when multiple parent classes define methods with the same name.
Python uses the C3 linearization algorithm to compute the MRO, which can be viewed using the __mro__ attribute or mro() method.
In this example, when super().display() is called in CustomerAccount, Python follows the MRO to decide which display() to execute first.

What to explain in this example:
--------------------------------
- How multiple inheritance allows a class to inherit from more than one parent class.
- How constructors from all parent classes are called (using direct calls and super()).
- How method overriding works in the context of multiple inheritance.
- How MRO determines which method is called when there are name conflicts.
- How to inspect the MRO using CustomerAccount.__mro__.

The script shows how Python determines which method to call (MRO) and how to use super() in a multiple inheritance context.
"""



# Base class
class Account:
    def __init__(self, acc_holder, acc_balance):
        self.holder = acc_holder
        self.balance = acc_balance
        print(f"Account created for {self.holder} with balance {self.balance}")

    def display(self):
        print(f"Account Holder: {self.holder}, Balance: {self.balance}")



# First parent class
class ATMCard:
    def __init__(self, card_number):
        self.card_number = card_number
        print(f"ATM Card issued: {self.card_number}")

    def card_info(self):
        print(f"ATM Card Number: {self.card_number}")



# Second parent class
class OnlineBanking:
    def __init__(self, online_id):
        self.online_id = online_id
        print(f"Online Banking enabled for ID: {self.online_id}")

    def online_info(self):
        print(f"Online Banking ID: {self.online_id}")



# Child class with multiple inheritance using super()
class CustomerAccount(OnlineBanking,ATMCard,Account):
    def __init__(self, acc_holder, acc_balance, card_number, online_id):
        # Directly call each parent constructor (simple, no **kwargs)
        Account.__init__(self, acc_holder, acc_balance)
        ATMCard.__init__(self, card_number)
        OnlineBanking.__init__(self, online_id)
        print(f"CustomerAccount created for {self.holder}")

    def display(self):
        # Demonstrate MRO: which display() is called?
        print("--- Customer Account Details ---")
        super().display()  # Calls Account.display due to MRO
        self.card_info()
        self.online_info()

        # Note: super() in multiple inheritance follows the MRO, so each parent class's __init__ is called once.
        # This is safer and more maintainable than direct parent class calls, especially in complex hierarchies.

if __name__ == "__main__":
    # Create a CustomerAccount instance
    cust_acc = CustomerAccount("Charlie", 5000, "ATM12345", "ONLINE6789")
    cust_acc.display()

    # Show the MRO for CustomerAccount
    print("\nMRO for CustomerAccount:")
    for cls in CustomerAccount.__mro__:
        print(cls)

    # Output demonstrates multiple inheritance and MRO

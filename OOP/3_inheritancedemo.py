"""
3_inheritancedemo.py
--------------------
This script demonstrates single inheritance, method overriding, and the use of super() in Python.
A real-time example using a Bank scenario is provided.

Key Concepts:
1. Single Inheritance
2. Method Overriding
3. Using super() to call the parent class method

Scenario:
- BankAccount: Base class representing a generic bank account
- SavingsAccount: Derived class representing a savings account with interest
"""

# Base class
class BankAccount:
    def __init__(self, acc_holder, acc_balance):
        """
        Constructor for BankAccount.
        Parameters:
            acc_holder: Name of the account holder
            acc_balance: Initial balance
        """
        self.holder = acc_holder
        self.balance = acc_balance
        print(f"BankAccount created for {self.holder} with balance {self.balance}")

    def deposit(self, amount):
        """Deposit money into the account."""
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance exists."""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display(self):
        """Display account details."""
        print(f"Account Holder: {self.holder}, Balance: {self.balance}")

# Derived class (Single Inheritance)
class SavingsAccount(BankAccount):
    def __init__(self, acc_holder, acc_balance, interest_rate):
        """
        Constructor for SavingsAccount.
        Calls the parent class constructor using super().
        Parameters:
            acc_holder: Name of the account holder
            acc_balance: Initial balance
            interest_rate: Interest rate for the savings account
        """
        super().__init__(acc_holder, acc_balance)  # Call parent constructor
        self.interest = interest_rate
        print(f"SavingsAccount created for {self.holder} with interest rate {self.interest}%")

    def add_interest(self):
        """Add interest to the balance."""
        interest_amount = self.balance * self.interest / 100
        self.balance += interest_amount
        print(f"Interest of {interest_amount} added. New balance: {self.balance}")

    def display(self):
        """
        Overridden method: Displays account details including interest rate.
        Calls the parent class display() using super().
        """
        super().display()  # Call parent display method
        print(f"Account Type: Savings, Interest Rate: {self.interest}%")

if __name__ == "__main__":
    # Create a BankAccount instance
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    acc.display()

    print("\n---\n")

    # Create a SavingsAccount instance
    sav_acc = SavingsAccount("Bob", 2000, 5)
    sav_acc.deposit(1000)
    sav_acc.add_interest()
    sav_acc.withdraw(500)
    sav_acc.display()

    # Output shows method overriding and use of super()

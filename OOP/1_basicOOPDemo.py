
"""
1_basicOOPDemo.py
-----------------
This script demonstrates basic Object-Oriented Programming (OOP) concepts in Python:

1. Class definition
2. Constructor (__init__)
3. Instance variables
4. Static (class) variables
5. Static method
6. Destructor (__del__)
7. The special block: if __name__ == "__main__"

Each concept is explained with comments and print statements for clarity.
"""

# Class definition
class Employee:
    # Static (class) variables: Shared by all instances of the class
    company_name = "JPMC"  # All employees belong to the same company
    employee_count = 0     # Tracks the number of Employee instances

    def __init__(self, emp_name, emp_code):
        """
        Constructor: Called automatically when a new object is created.
        Initializes instance variables (unique to each object).

        Parameters:
            emp_name: The name of the employee (passed during object creation)
            emp_code: The employee's code/ID (passed during object creation)

        Note on 'self':
            'self' is a reference to the current object (instance) being created or used.
            It allows access to the object's attributes and methods.
            The name 'self' is a convention, but it must be the first parameter of instance methods.
        """
        self.name = emp_name            # Instance variable, unique to each object
        self.code = emp_code            # Instance variable (renamed for clarity)
        Employee.employee_count += 1    # Increment class variable
        print(f"Employee {self.name} (Code: {self.code}) created.")

    def display(self):
        """
        Instance method: Can access both instance and class variables.
        Displays the details of the employee.
        """
        print(f"Name: {self.name}, Code: {self.code}, Company: {Employee.company_name}")

    @staticmethod
    def company_info():
        """
        Static method: Does not access instance variables (no 'self').
        Can be called on the class itself.
        Useful for utility functions related to the class.
        """
        print(f"Company Name: {Employee.company_name}")
        print(f"Total Employees: {Employee.employee_count}")

    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed (garbage collected).
        Used here to decrement the employee count and print a message.
        Note: In CPython, __del__ is called when the reference count reaches zero,
        but its execution time is not guaranteed.
        """
        Employee.employee_count -= 1
        print(f"Employee {self.name} (Code: {self.code}) deleted.")

# Example usage
# The following block ensures that this code runs only when the script is executed directly,
# and not when it is imported as a module in another script.
#
# __name__ is a special built-in variable in Python. When a script is run directly,
# __name__ is set to "__main__". When imported, it is set to the module's name.


if __name__ == "__main__":
    # Creating instances of Employee (note the parameter names now match the constructor)
    emp1 = Employee("Alice", 101)
    emp2 = Employee("Bob", 102)

    # Accessing instance method to display employee details
    emp1.display()
    emp2.display()

    # Accessing static method to display company info
    Employee.company_info()

    # Deleting an instance (calls destructor)
    del emp1
    # Display company info again to show updated employee count
    Employee.company_info()

    # Note: The destructor (__del__) may not be called immediately upon program exit for all objects.

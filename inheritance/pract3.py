class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment   # increment in percentage

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, newSalary):
        # Calculate increment percentage needed to reach newSalary
        self.increment = ((newSalary - self.salary) / self.salary) * 100
emp = Employee(20000, 10)

print("Old increment:", emp.increment)
print("Salary after increment:", emp.salaryAfterIncrement)

# User sets a new final salary
emp.salaryAfterIncrement = 25000

print("New increment:", emp.increment)
print("New salary after increment:", emp.salaryAfterIncrement)

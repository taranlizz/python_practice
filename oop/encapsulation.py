"""
Encapsulation:
binding data(attributes) and the methods(functions) that operate
on that data into a single unit - the class.
It also involves restricting direct access to some of the object's components,
which is important for data hiding and code integrity.
"""


# Example without encapsulation
class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance


# No error, even though the balance cannot be negative.
account = BadBankAccount(0)
account.balance = -1


# Example with encapsulation
class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


account = BankAccount()
# Error, the balance property doesn't have a setter function.
account.balance = -1

from abc import ABC, abstractmethod

# Abstract class (Abstraction)
class BankAccount(ABC):
    bank_name = "ABC Bank"   # class-level parameter

    def __init__(self, name, balance):
        self.name = name            # public attribute
        self._account_type = "Savings"  # protected attribute
        self.__balance = balance    # private attribute (encapsulation)

    @abstractmethod
    def account_info(self):
        pass

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")

# Child class (Inheritance + super)
class SavingsAccount(BankAccount):
    interest_rate = 5  # class-level parameter

    def __init__(self, name, balance):
        super().__init__(name, balance)  # call parent constructor

    # Overriding abstract method (Polymorphism)
    def account_info(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Type: {self._account_type}")  # protected
        print(f"Bank: {self.bank_name}")  # class-level parameter

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print(f"Adding interest: {interest}")
        self.deposit(interest)

# Another Child class (Polymorphism)
class CurrentAccount(BankAccount):
    interest_rate = 2

    def __init__(self, name, balance):
        super().__init__(name, balance)

    def account_info(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Type: Current")
        print(f"Bank: {self.bank_name}")

# Using objects
s_acc = SavingsAccount("Alice", 1000)
c_acc = CurrentAccount("Bob", 2000)

# Access public & private through methods
s_acc.deposit(500)
s_acc.add_interest()
s_acc.account_info()

print("\n---\n")

c_acc.deposit(1000)
c_acc.account_info()
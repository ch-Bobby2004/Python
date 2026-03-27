# Parent class
class Bank:
    def __init__(self, name, balance):
        self.name = name               # public attribute
        self.__balance = balance       # private attribute (encapsulation)

    def get_balance(self):             # public method to access private data
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")

# Child class inheriting Bank
class SavingsAccount(Bank):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)   # super() calls parent constructor
        self._interest_rate = interest_rate  # protected attribute

    def add_interest(self):
        interest = self.get_balance() * self._interest_rate / 100
        print(f"Adding interest: {interest}")
        self.deposit(interest)

# Using objects
acc = SavingsAccount("Alice", 1000, 5)   # create object
print(acc.name)                           # access public attribute
print(acc.get_balance())                  # access private attribute via method

acc.deposit(500)                          # deposit money
acc.add_interest()                        # add interest using method
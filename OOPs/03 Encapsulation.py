# Encapsulation = hiding data + controlling access to it

# You don’t allow direct access to some variables.
# Instead, you use methods (functions) to access or change them.



class Bank:
    def __init__(self):
        self.balance = 1000   # not private

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def get_balance(self):
        return self.balance

b = Bank()
b.deposit(500)
print(b.get_balance())






class Bank:
    def __init__(self):
        self.__balance = 1000   # private variable

    def get_balance(self):
        return self.__balance

b = Bank()
print(b.get_balance())





# __balance → private variable
# You cannot access it directly:
# print(b.__balance)  # ❌ Error


# Why Encapsulation?
# Protects data 
# Prevents mistakes
# Gives control over how data is used


# Encapsulation = hide data and access it using methods
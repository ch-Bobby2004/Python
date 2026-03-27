# balance → Public
class Bank:
    def __init__(self):
        self.balance = 1000
        
b = Bank()
print(b.balance)   # works

# Anyone can read/write it
# No restriction



# _balance → Protected (just a warning ⚠️)
class Bank:
    def __init__(self):
        self._balance = 1000

#  You can still access it:

print(b._balance)   # works

# It’s not truly private
# It’s just a convention (means: “please don’t touch from outside”)





# . __balance → Private (Name Mangling 🔒)
class Bank:
    def __init__(self):
        self.__balance = 1000

# 👉 Direct access will fail:

print(b.__balance)   # ❌ Error


# Python changes name internally to:

print(b._Bank__balance)   # ✅ Works (but not recommended)

# 👉 This is called name mangling
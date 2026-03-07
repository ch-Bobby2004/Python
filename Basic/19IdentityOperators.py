a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True → same object
print(a is c)     # False → different objects
print(a == c)     # True → values are equal
# Key point: == checks values, is checks object identity.

x = 5
y = 5

print(x is y)     # True (small integers are cached in Python)
print(x is not y)     
print(x == y)     # True
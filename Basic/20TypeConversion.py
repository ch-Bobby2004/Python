# Implicit Type Conversion

x = 5       # int
y = 2.0     # float

result = x + y
print(result)        # 7.0
print(type(result))  # float



x = 100
y = str(x)

print(y)        # "100"
print(type(y))  # str
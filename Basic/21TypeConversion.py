# Explicit Type Conversion (Type Casting)
x = "10"
y = int(x)

print(y)        # 10
print(type(y))  # int


x = "3.14"
y = float(x)

print(y)        # 3.14


x = "hello"

print(list(x))   # ['h','e','l','l','o']
print(tuple(x))  # ('h','e','l','l','o')
print(set(x))    # {'h','e','l','o'}
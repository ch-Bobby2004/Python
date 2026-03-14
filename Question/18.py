n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Sum:", sum(numbers))



nums = input("Enter numbers separated by space: ").split()

total = 0
for n in nums:
    total += int(n)

print("Sum:", total)


from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print("Sum:", total)

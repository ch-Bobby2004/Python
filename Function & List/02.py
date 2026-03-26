# Sum of elements in a list
my_list = [4, 7, 1, 9, 3]
total = 0

for num in my_list:
    total += num

print("Sum of list:", total)

my_list = [4, 7, 1, 9, 3]

total = sum(my_list)
print("Sum of list:", total)



def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

my_list = [4, 7, 1, 9, 3]
print("Sum of list:", list_sum(my_list))
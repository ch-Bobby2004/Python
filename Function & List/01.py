# maximum element of a list using a function

my_list = [4, 7, 1, 9, 3]

maximum = max(my_list)
print("Maximum element:", maximum)


def find_max(lst):
    max_val = lst[0]  # Assume first element is max
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

my_list = [4, 7, 1, 9, 3]
print("Maximum element:", find_max(my_list))
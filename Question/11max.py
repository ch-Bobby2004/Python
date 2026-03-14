arr = [10, 25, 7, 89, 45]
print(max(arr))


arr = [10, 25, 7, 89, 45]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)


arr = [10, 25, 7, 89, 45]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)
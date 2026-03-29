def is_sorted(arr, n):
    # Base case
    if n == 1:
        return True
    
    # If last element is smaller than previous → not sorted
    if arr[n-1] < arr[n-2]:
        return False
    
    # Recursive check for remaining array
    return is_sorted(arr, n-1)

# Example
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr, len(arr)))  # True
'''
Binary Search using Recursion:
Write a recursive Python function called `binary_search` that takes a sorted list and a 
target value as input and returns the index of the target value in the list using binary search.
Return -1 if the target is not found.
'''

def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Target not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

# Taking input from the user
arr = list(map(int, input("Enter a sorted list of numbers separated by spaces: ").split()))
target = int(input("Enter the target value to search for: "))

# Call the function and print the result
index = binary_search(arr, target, 0, len(arr) - 1)
if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found in the list")
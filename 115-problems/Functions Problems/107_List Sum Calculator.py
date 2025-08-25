'''
List Sum Calculator:
Write a Python function called `list_sum` that takes a list of integers as input 
and returns the sum of all elements in the list. Test the function with different lists.
'''

def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Test the function
nums = [10, 20, 30, 40]
print(f"The sum of {nums} is {list_sum(nums)}.")

# Another test
nums2 = [5, 15, 25]
print(f"The sum of {nums2} is {list_sum(nums2)}.")
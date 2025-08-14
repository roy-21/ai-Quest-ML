'''
28. List Manipulation: Given a list of integers, write a Python program 
using a for loop to find the sum, average, maximum, and minimum values in 
the list.
'''


numbers = list(map(int, input("Enter space-separated integers: ").split()))

total = 0
max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    total += num
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

average = total / len(numbers)

print("Sum:", total)
print("Average:", average)
print("Maximum:", max_val)
print("Minimum:", min_val)

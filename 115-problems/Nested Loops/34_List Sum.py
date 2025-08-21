n = int(input("Enter number of elements: "))

numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

total = sum(numbers)
print("Sum of the list:", total)

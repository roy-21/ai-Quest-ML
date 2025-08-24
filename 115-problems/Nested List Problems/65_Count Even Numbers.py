'''
Count Even Numbers: Write a Python program to count the number of even
numbers in a nested list.
'''

#User input
n = int(input("Enter number of sublists: "))

nested_list = []
for i in range(n):
    sublist = list(map(int, input(f"Enter elements of sublist {i+1} separated by space: ").split()))
    nested_list.append(sublist)

#Count even numbers
even_count = 0
for sub in nested_list:
    for num in sub:
        if num % 2 == 0:
            even_count += 1

#result
print("Total Even Numbers:", even_count)
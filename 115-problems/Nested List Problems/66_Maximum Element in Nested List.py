'''
Maximum Element in Nested List: Write a Python program to find the maximum 
element in a nested list of integers.
'''

#User input
n = int(input("Enter number of sublists: "))

nested_list = []
for i in range(n):
    sublist = list(map(int, input(f"Enter elements of sublist {i+1} separated by space: ").split()))
    nested_list.append(sublist)

#Find maximum element
max_element = nested_list[0][0]  #assume first element is max
for sub in nested_list:
    for num in sub:
        if num > max_element:
            max_element = num

#result
print("Maximum Element:", max_element)
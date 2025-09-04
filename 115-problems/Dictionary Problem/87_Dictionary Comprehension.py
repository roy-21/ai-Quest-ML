'''
Dictionary Comprehension: Given a list of integers, write a Python program to create 
a dictionary where the keys are the elements from the list, and the values are their squares.
'''

numbers = list(map(int, input("Enter integers separated by space: ").split()))

#Create dictionary using comprehension
squares_dict = {num: num ** 2 for num in numbers}

#Print the result
print("Dictionary with numbers and their squares:")
print(squares_dict)
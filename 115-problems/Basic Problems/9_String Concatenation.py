'''
9. String Concatenation: Write a Python program that 
takes two strings as input and concatenates them into a 
single string without using the `+` operator.
'''

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = "".join([str1, str2])
print(result)

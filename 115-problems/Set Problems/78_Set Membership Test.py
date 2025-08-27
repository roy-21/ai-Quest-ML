'''
Set Membership Test: Write a Python program that takes an element as input 
and checks if it exists in a given set. Print “Found” if the element is present 
and “Not Found” otherwise.
'''

user_set = set(input("Enter elements of the set separated by space: ").split())

#Input for the element to check
element = input("Enter the element to check: ")

#Membership test
if element in user_set:
    print("Found")
else:
    print("Not Found")
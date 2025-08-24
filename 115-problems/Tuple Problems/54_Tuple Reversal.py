'''
Tuple Reversal: Write a Python program to reverse a tuple without using any built-in
functions.
'''

#input
t = tuple(input("Enter elements of the tuple separated by space: ").split())

# reverse tuple using loop
reversed_tuple = ()
for item in t:
    reversed_tuple = (item,) + reversed_tuple
print("Reversed tuple:", reversed_tuple)
'''
Positive Number Sum: Write a Python program that takes positive numbers as 
input until a negative number is entered. Then, calculate and print the sum 
of all positive numbers entered. Use a `while` loop and `break` to exit 
the loop when a negative number is encountered.
'''

total = 0

while True:  
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:    
        break
    total += num      

print("Sum of positive numbers:", total)
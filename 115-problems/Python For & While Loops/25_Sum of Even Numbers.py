'''
25. Sum of Even Numbers: Write a Python program using a while loop to 
calculate the sum of all even numbers between 1 and N, where N is taken 
as input from the user
'''


N = int(input("Enter the value of N: "))
i = 1
even_sum = 0

while i <= N:
    if i % 2 == 0:
        even_sum += i
    i += 1
    
print(even_sum)

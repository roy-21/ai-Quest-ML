'''
23. Count Digits in a Number: Write a Python program using a while loop to 
count the number of digits in a given integer N.
'''


N = int(input("Enter a number:"))
if N == 0:
    count = 1
else:
    count = 0
    N = abs(N)
    while N > 0:
        N //= 10
        count += 1
print(count)
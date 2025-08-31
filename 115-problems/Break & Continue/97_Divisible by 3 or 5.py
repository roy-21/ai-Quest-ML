'''
Divisible by 3 or 5
'''

for num in range(1, 51):   
    if num % 3 != 0 and num % 5 != 0:   
        continue                       
    print(num)
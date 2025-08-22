n = int(input())
arr = list(map(int, input().split()))

x = int(input())

count = 0
for num in arr:
    if num == x:
        count += 1
print(count)

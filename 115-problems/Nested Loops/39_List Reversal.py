n = int(input())
arr = list(map(int, input().split()))

reversed_list = []
for i in range(n-1, -1, -1):
    reversed_list.append(arr[i])
print(*reversed_list)

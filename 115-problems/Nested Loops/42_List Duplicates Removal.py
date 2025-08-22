n = int(input())
arr = list(map(int, input().split()))

unique_list = []
seen = set()
for num in arr:
    if num not in seen:
        unique_list.append(num)
        seen.add(num)
print(*unique_list)
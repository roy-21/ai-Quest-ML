n1 = int(input())
list1 = list(map(int, input().split()))

n2 = int(input())
list2 = list(map(int, input().split()))

common = []
for elem in list1:
    if elem in list2 and elem not in common:
        common.append(elem)
print(*common)

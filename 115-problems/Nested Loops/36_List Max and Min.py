n = int(input())
arr = list(map(int, input().split()))

maximum = arr[0]
minimum = arr[0]

for num in arr[1:]:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Max:", maximum)
print("Min:", minimum)

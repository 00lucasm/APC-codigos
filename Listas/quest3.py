a = list(map(int, input().split()))
i, j = input().split()
i = int(i)
j = int(j)
within_interval = []
out_of_interval = []

for number in a:
    if (number >= i) and (number <= j):
        within_interval.append(number)
    else:
        out_of_interval.append(number)

print(within_interval)
print(out_of_interval)
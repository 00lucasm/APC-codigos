N = input()
N = int(N)

a = list(map(int, input().split()))

t_min = sorted(a)
t_min = t_min[0]

for i in range(len(a)):
    a[i] = a[i] - t_min

print(*a) # THIS IS VERY INTERESTING...
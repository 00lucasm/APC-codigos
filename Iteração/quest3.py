n, m = input().split()

n = int(n)
m = int(m)
exp = 1

while(n**exp <= m):
    print(n**exp)
    exp = exp + 1

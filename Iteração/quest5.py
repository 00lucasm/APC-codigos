
n = int(input())
N = 0
soma = 0

while(n != -1):
    soma += n
    N += 1
    n = int(input())

print(soma//N)

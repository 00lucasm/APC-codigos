#!/usr/bin/python3

# n é o tamanho da lista
# m é o número de consultas
n, m = input().split()
n = int(n)
m = int(m)

a = list(map(int, input().split()))

while(m > 0):
    i, j = input().split()
    i = int(i)
    j = int(j)
    a[i] = j
    print(a)
    m -= 1
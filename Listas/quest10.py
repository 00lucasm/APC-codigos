n = int(input())
lista = list(map(int, input().split()))

control = 'nao'

for i in range(len(lista)):
    for j in range(len(lista)):
        if (lista[i] + lista[j]) == 42:
            control = 'sim'

print(control)
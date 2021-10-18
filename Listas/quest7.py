lista = list(map(int, input().split()))

i = 1
control = 'False'

for i in range(len(lista)):
    if i in lista:
        lista.remove(i)
        if i in lista:
            control = 'True'
            break

print(control)
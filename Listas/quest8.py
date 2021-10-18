premios = list(map(int, input().split()))
valor_sorteado = int(input())

premios.sort()

for elemento in premios:
    if elemento > valor_sorteado:
        premios.pop()

if sum(premios) >= valor_sorteado:
    print('E possivel ganhar.')
else:
    print('Impossivel ganhar.')
def soma_aninhada(lista):
    soma = 0
    for i in range(len(lista)):
        soma += sum(lista[i])
    return soma
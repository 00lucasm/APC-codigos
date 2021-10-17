'''
Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Exemplo:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
>>> 21
'''
def nested_sum(t):
    soma = 0
    for i in range(len(t)):
        soma += sum(t[i])
    return soma

lista = [[0, 0], [0, 0], [0, 0, 0]]
print(nested_sum(lista))
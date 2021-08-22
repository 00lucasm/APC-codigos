'''
Entrada: valores inteiros x e y, com x correspondendo à quantidade de pares de botas
e y correspondendo à quantidade de chapéus

Saída: quantidade máxima de peças nos jogos de vestimentas
'''
def vestimentas(x_botas, y_chapeus):
    if(x_botas >= y_chapeus):
        print(y_chapeus*2)
    else:
        print(x_botas*2)

# TESTES:
#x = int(input())
#y = int(input())

#vestimentas(x, y)
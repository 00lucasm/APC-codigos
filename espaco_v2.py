'''
Implemente um programa que troca a ordem de apresentação de dois números, de um total de 5 pares de números. Seu programa deve ler 5 pares de números inteiros e para cada um deles deverão ser impressos os números com a ordem trocada. A função responsável por realizar essa operação deverá chamar trocarAB e receber dois valores numéricos.
'''
def trocarAB(A, B):
    print(f'{B} {A}')

x0, y0 = input().split()
x0 = int(x0)
y0 = int(y0)

x1, y1 = input().split()
x1 = int(x1)
y1 = int(y1)

x2, y2 = input().split()
x2 = int(x2)
y2 = int(y2)

x3, y3 = input().split()
x3 = int(x3)
y3 = int(y3)

x4, y4 = input().split()
x4 = int(x4)
y4 = int(y4)

trocarAB(x0, y0)
trocarAB(x1, y1)
trocarAB(x2, y2)
trocarAB(x3, y3)
trocarAB(x4, y4)

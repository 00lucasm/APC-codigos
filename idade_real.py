'''
Idade Real
Entrada: três números inteiros 1 <= d1, d2, d3 <= 10^6
Saída: para cada uma das três idades deve ser imprimido três inteiros separados por espaço:
A M D
representando a idade da pessoa em anos, meses e dias, respectivamente
'''
def age(idade_em_dias):
    anos = idade_em_dias//360
    meses = ((idade_em_dias%360)//30)
    dias = ((idade_em_dias%360)%30)
    print(f'{anos} {meses} {dias}')

d1, d2, d3 = input().split()

d1 = int(d1)
age(d1)
d2 = int(d2)
age(d2)
d3 = int(d3)
age(d3)

# definindo uma função em python

def media(n1, n2, n3):
	soma = n1 + n2 + n3
	resultado = soma / 3
	return resultado

nota1 = float(input('Insira a nota 1: '))
nota2 = float(input('Insira a nota 2: '))
nota3 = float(input('Insira a nota 3: '))

# print(round(media_ponderada, 6))
# print(round(media(nota1, nota2, nota3), 1))
print(f'A média é {round(media(nota1, nota2, nota3), 1)}')

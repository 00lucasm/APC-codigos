# média ponderada
le_numeros = list(map(float, input().split()))
le_pesos = list(map(int, input().split()))

n1 = le_numeros[0]
n2 = le_numeros[1]
n3 = le_numeros[2]

p1 = le_pesos[0]
p2 = le_pesos[1]
p3 = le_pesos[2]

media_ponderada = (n1*p1 + n2*p2 + n3*p3)/(p1 + p2 + p3)

# print("%.6f" % media_ponderada)
print(round(media_ponderada, 6))

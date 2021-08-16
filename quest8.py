# média ponderada
n1, n2, n3 = input().split() # leitura de valores numa linha separados por espaço ' '
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

p1, p2, p3 = input().split()
p1 = int(p1)
p2 = int(p2)
p3 = int(p3)

media_ponderada = (n1*p1 + n2*p2 + n3*p3)/(p1 + p2 + p3)

# print("%.6f" % media_ponderada)
print(round(media_ponderada, 6))

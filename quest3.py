# ENTRADA: consiste de três caracteres alfanuméricos x, y e z, um por linha, sendo esses letra do alfabeto latino, maiúscula, minúscula ou dígito

x = input()
y = input()
z = input()

# saída1: caracteres lidos juntos
print(x + y + z)

# saída2: somente o primeiro caractere lido
print(x)

# saída3: duas vezes o segundo caractere lido
print(y*2)

# saída4: três vezes o terceiro caractere, separados por um espaço:
print(f'{z} {z} {z}')

# saída5: a mensagem "X == x, Y == y, Z == z"
print(f'X == {x}, Y == {y}, Z == {z}')

# saída6: a mensagem "X != y, Y != x, Z == z"
print(f'X != {y}, Y != {x}, Z == {z}')

"""
STRINGS == cadeia de caracteres!
"""

def palindromo(frase):
    return frase == frase[::-1]

# Início do programa

frase = input("Digite uma frase: ")
# palavra = input("Digite uma palavra: ")

print(f'É palíndromo? {palindromo(frase)}')

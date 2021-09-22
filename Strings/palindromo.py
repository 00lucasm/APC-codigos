#!/bin/python3
"""
STRINGS == cadeia de caracteres!
"""
# essa função só funciona para strings
def palindromo_string(frase):
    return frase == frase[::-1]

def palindromo(frase):
    frase = frase.replace(' ','')
    return frase.lower() == frase[::-1].lower()

# Conta quantas vezes string ocorre em frase
def busca_string(frase, string):
    cont = 0
    i = -1
    while True:
        i = frase.find(string, i + 1)
        if i == -1:
            return cont
        else:
            cont += 1

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

# print(f'É uma string palíndromo? {palindromo_string(frase)}')
# print(f'É uma frase palíndromo? {palindromo(frase)}')

print(f'Possui {busca_string(frase, palavra)} ocorrências da string "{palavra}"')

frase = input()

palavras = list(frase.split(' '))

print(palavras)

for palavra in palavras:
    if len(palavra) > 6:
        print(palavra)

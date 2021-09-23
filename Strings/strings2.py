"""STRINGS

Vamos "cebolinhar" uma frase? A ideia é trocar a frase pela sua versão
"correta" segundo o Cebolinha!
Para atl devemos trocar as letras 'r' por 'l', mas tem mais uns detalhes...
r -> l
R -> L
rr -> l
RR -> L
"""

def cebolinhar(frase):
    nova_frase = ''

    for letra in frase:
        nova_frase += letra

    return nova_frase

frase = input("Escreva uma frase: ")
print(f'O Cebolinha diria: {cebolinhar(frase)}')

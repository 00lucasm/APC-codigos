'''
Vanessa e o ano bonito
Um dia, Vanessa estava lendo jornal quando leu uma curiosidade: após 1987, o ano de 2013 é o primeiro a ter apenas dígitos distintos. A partir desse momento, Vanessa passou a considerar isso um ano bonito. Quando isso aconteceu, Vanessa vivia no ano x, e se perguntou, qual é o próximo ano bonito?

Entrada
A única linha de entrada contém um inteiro 0≤x≤9999. O ano em que Vanessa se encontra.

Saída
Imprima um único inteiro: a resposta do problema.

Notas

No primeiro exemplo de teste, o próximo ano bonito em relação a x=1987 é 2013, pois 2013 é o menor número maior do que 1987 em que todos os seus dígitos são distintos. Observe que na sequência de anos após 1987, dada pelos anos 1988,1989,1990,1991,1992,1993,…2011,2012 sempre encontramos algum dígito repetido no ano.

No segundo exemplo de teste, o próximo ano bonito para a entrada x=444 é 450, pois conforme a sequência de anos 445,446,447,448,449…450, o ano 450 possui todos os seus dígitos distintos. 
'''

value = int(input())
base = 1000

while(value % base) > 0:
    tmp = value // base
    value = value % base
    base = base // 10
    print(tmp)

'''
Iteração ou recursão
Leia um inteiro n, enquanto n for positivo, imprima "estou dentro de um loop while ou em uma recursao?" e decremente o n em 1.

Entrada
A entrada contém um único inteiro positivo n (1≤n≤100), como descrito no enunciado.

Saída
Faça um loop while imprimindo a mensagem pedida.

Observações
No primeiro exemplo de teste, a resposta é apenas uma repetição pois n é igual a 1.
'''
n = int(input())

while(n > 0):
    print("estou dentro de um loop while ou em uma recursao?")
    n = n - 1



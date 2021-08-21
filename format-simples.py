# dados dois números inteiros a e b, apresente o resultado da divisão deles com uma precisão p arbitrária

a = int(input())
b = int(input())
precision = int(input())

print(round(a/b, precision))

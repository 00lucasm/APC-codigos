# Cálculo de Potência v1
# implemente um programa que calcule x^y
# x e y são valores de entrada inteiros

import math

x, y = input().split()

x = int(x)
y = int(y)

print(float(pow(x, y)))

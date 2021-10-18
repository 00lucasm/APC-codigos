from math import sqrt

N = list(map(int, input().split()))

media = sum(N)/len(N)

for i in range(len(N)):
    N[i] = (N[i] - media)**2

desvio_padrao = sqrt(sum(N)/len(N))

print(round(media, 1))
print(round(desvio_padrao, 1))

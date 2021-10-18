N = int(input()) # total de figurinhas a preencher no álbum
M = int(input()) # número de figurinhas já compradas

album = []
album.extend(range(1, N+1)) # preenche a lista com inteiros de 1 a N+1

compradas = []

while(M > 0):
    x = int(input())
    if not(x in compradas):
        compradas.append(x)
        if x in album:
            album.remove(x)
    M -= 1

print(len(album))

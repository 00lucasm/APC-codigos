
def mdc(x, y):
    if(x%y == 0):
        return y
    else:
        return mdc(y, x%y)

a, b = input().split()

a = int(a)
b = int(b)

if(mdc(a, b) == 1):
    print("Sao co-primos.")
else:
    print("Nao sao co-primos!")

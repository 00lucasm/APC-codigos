
def mdc(x, y):
    if(y == 0):
        return x
    elif((x%y > 0) & (y > 0)):
        return mdc(y, x%y)

a = int(input())
b = int(input())

print(mdc(a, b))


def mdc(x, y):
    if(x == 0):
        return x;
    elif(x%y > 0):
        return mdc(x, x%y)

a = int(input())
b = int(input())

print(mdc(a, b))

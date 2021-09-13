
def mdc(x, y):
    if(x%y == 0):
        return y
    else:
        return mdc(y, x%y)

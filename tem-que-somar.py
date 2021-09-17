def count_1s(X):
    counter = 0
    if(X == 0):
        return counter
    else:
        if(X%2 == 1):
            counter = counter + 1
            
        return count_1s(X//2)
        
a = int(input())
print(count_1s(a))
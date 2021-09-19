#!/usr/bin/python3
a = int(input("> Insert a value!\n> "))

while(a <= 0):
    print("> Please, insert a value greater than ZERO!")
    a = int(input())

print(f"{a*10}")

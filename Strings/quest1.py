#!/usr/bin/python3

# lexical order between strA and strB
def lo(strA, strB):
    if strA >= strB:
        return strA+strA
    else:
        return strB+strB

s = input()

primeira_metade = s[0:(len(s)//2)]
segunda_metade = s[(len(s)//2):len(s)]

print(lo(primeira_metade, segunda_metade))

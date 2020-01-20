C = str(input())
alphabet=list('abcdefghijklmnopqrstuvwxyz')

index = alphabet.index(C)
if index==25:
    index=-1
print(alphabet[index+1])

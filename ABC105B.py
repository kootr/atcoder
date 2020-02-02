N = int(input())
for f in range(0,26):
    for s in range(0,15):
        if (4*f)+(7*s)==N:
            print('Yes')
            break
        elif (f==25) and (s==14):
            print('No')
    else:
        continue
    break
H, N = map(int, input().split())
Asum = sum([a for a in map(int,input().split())])
if H > Asum:
    print('No')
else:
    print('Yes')
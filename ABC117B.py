N = int(input())
L = list(map(int, input().split()))
if max(L) < (1/2)*sum(L):
    print('Yes')
else:
    print('No')
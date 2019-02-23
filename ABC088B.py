n = int(input())
x = list(map(int, input().split()))
y = sorted(x, reverse = True)
alice = 0
bob = 0
for i in range(0,n,2):
    alice += y[i]
for j in range(1,n,2):
    bob += y[j]
print(alice - bob)

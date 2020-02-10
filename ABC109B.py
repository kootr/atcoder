import sys
N = int(input())
W = []
for i in range(N):
    W.append(input())
if len(set(W)) != len(W):
    print("No")
else:
    for i in range(len(W)-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            sys.exit()
    print("Yes")

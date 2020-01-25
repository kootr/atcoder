N = int(input())
P = list(map(int, input().split(" ")))
cnt = 0
S = P[0]
for i in range(N):
    if S >= P[i]:
        cnt += 1
    S = min(S, P[i])

print(cnt)
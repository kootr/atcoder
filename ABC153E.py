H, N = map(int, input().split())
S = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    S[i].append(S[i][0]/S[i][1])
S.sort(key=lambda S:S[2])
print(S)

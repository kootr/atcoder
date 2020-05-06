N = int(input())
S, T = map(list, input().split())
U = []
# print(S, T)
for i in range(N):
    U.append(S[i]+T[i])

print(''.join(U))
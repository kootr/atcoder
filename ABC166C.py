N, M = map(int, input().split())
H = list(map(int, input().split()))
heighest = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    heighest[a-1] = max(heighest[a-1], H[b-1])
    heighest[b-1] = max(heighest[b-1], H[a-1])

cnt = 0

for i, j  in zip(heighest, H):
    if i < j:
        cnt += 1
print(cnt)

# N, M = map(int, input().split())
# H = list(map(int, input().split()))
 
# A = [0] * N
# for i in range(M):
#     a, b = map(int, input().split())
#     A[a - 1] = max(A[a - 1], H[b - 1])
#     A[b - 1] = max(A[b - 1], H[a - 1])
 
# ans = sum(H[i] > A[i] for i in range(N))
# print(ans)
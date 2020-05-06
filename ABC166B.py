N, K = map(int, input().split())
d = []
A = []
for i in range(K):
    d.append(int(input()))
    A.append(list(map(int, input().split())))
have_sweet = set(sum(A, []))
all_member = set([i for i in range(1, N+1)])
print(len(have_sweet ^ all_member))
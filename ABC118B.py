n, m = map(int, input().split())
A = set({i for i in range(1,m+1)})
for i in range(n):
    row = list(map(int, input().split()))
    k = row[0]
    A_i = row[1:]
    A = A & set(A_i)
print(len(list(A)))
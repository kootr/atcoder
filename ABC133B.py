import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(int(N))]
cnt = 0

for i in range(N):
    for j in range(i+1, N):
        length = 0
        for x_i, x_j in zip(X[i], X[j]):
            length += (x_i-x_j)**2
        length = math.sqrt(length)
        if length == int(length):
            cnt += 1

print(cnt)
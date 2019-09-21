import numpy as np
N, M, C = [int(i) for i in input().split()]
B = np.array([int(i) for i in input().split()])
A = []
cor = 0
for i in range(N):
    A = np.array([int(j) for j in input().split()])
    if (sum(A*B) + C) > 0:
        cor += 1
        A = []
    else:
        A = []
print(cor)

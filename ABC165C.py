import itertools
N, M, Q = map(int, input().split())
a_b_c_d = [list(map(int, input().split())) for i in range(Q)]

M = [i for i in range(1, M+1)]
A_possible = list(itertools.combinations_with_replacement(M, N))

A_score = 0
for A in A_possible:
    A_sum = 0
    for i in range(Q):
        A_test = A[a_b_c_d[i][1]-1] - A[a_b_c_d[i][0]-1]
        if A_test == a_b_c_d[i][2]:
            A_sum += a_b_c_d[i][3]
    if A_score < A_sum:
        A_score = A_sum
print(A_score)
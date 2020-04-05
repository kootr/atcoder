N, K = map(int, input().split())
n_1 = N - (K * (N // K))
n_2 = abs(n_1 - K)
print(min(n_1, n_2))
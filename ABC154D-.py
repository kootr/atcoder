N, K = map(int, input().split())
p = list(map(int, input().split()))
SUM_P = [sum(p[i:i+K]) for i in range(N-K+1)]
print((max(SUM_P)+K)/2)
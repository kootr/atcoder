N, K = map(int, input().split())
p = list(map(int, input().split()))
SUM_P=sum(p[0:K])
all_sum_p=[SUM_P]
for i in range(N-K):
    SUM_P=SUM_P-p[i]+p[i+K]
    all_sum_p.append(SUM_P)
print((max(all_sum_p)+K)/2)
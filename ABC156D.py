from scipy.special import comb
n, a, b = map(int, input().split())

sum_c=0
for i in range(1,n+1):
    sum_c += comb(n, i, exact=True)
sum_c = sum_c - comb(n, a, exact=True) -comb(n, b, exact=True)
print(sum_c%(10**9+7))
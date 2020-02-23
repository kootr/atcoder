N = int(input())
X = list(map(int, input().split()))
X_min = min(X)
X_max = max(X)
S = []
for base_point in range(X_min, X_max+1):
    sum_X = 0
    for X_i in X:
        sum_X += (X_i-base_point)**2
    S.append(sum_X)
print(min(S))

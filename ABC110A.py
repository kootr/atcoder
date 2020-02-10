# A, B, C = map(int, input().split())
X = input().split()
X = [int(i) for i in X]
X.sort(reverse=True)
sum = X[0]*10 + X[1] + X[2]
print(sum)
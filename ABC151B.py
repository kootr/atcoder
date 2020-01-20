#n-1 科目の得点を代入する回数に制限がない
N, K, M = map(int, input().split(" "))
A = [int(i) for i in input().split(" ")]
A_n = M*N - sum(A)
if A_n > K:
    print('-1')
elif A_n < 0:
    print(0)
else:
    print(A_n)
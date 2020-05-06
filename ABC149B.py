A, B, K =map(int, input().split())
if K <= A:
    print(A-K, B)
elif A+B <= K:
    print(0, 0)
else:
    print(0, A+B-K)
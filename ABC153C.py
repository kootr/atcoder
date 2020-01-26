N, K = map(int, input().split())
H = [h for h in map(int, input().split())]
H.sort()
if N-K <= 0:
    print(0)
else:
    print(sum(H[:N-K]))
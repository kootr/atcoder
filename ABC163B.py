N, M = map(int, input().split())
A = list(map(int, input().split()))
play = N - sum(A)
if play >= 0:
    print(play)
else:
    print(-1)

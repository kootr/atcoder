from itertools import permutations

N = int(input())
R = list(permutations(range(1,N+1)))
P = tuple(map(int, input().split(" ")))
Q = tuple(map(int, input().split(" ")))
print(abs(R.index(P)-R.index(Q)))
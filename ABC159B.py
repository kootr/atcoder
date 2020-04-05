S = list(input())
N = len(S)
if S[:int((N-1)/2)] == list(reversed(S[:int((N-1)/2)]))\
    and S[int((N+1)/2):] == list(reversed(S[int((N+1)/2):]))\
    and S == list(reversed(S)):

    print('Yes')
else:
    print('No')
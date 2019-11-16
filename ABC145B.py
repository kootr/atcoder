N = int(input())
if N % 2 ==1:
    print('No')
    exit
else:
    S = str(input())
    n = int(N / 2)
    former_S = S[:n]
    latter_S = S[n:]
    if former_S == latter_S:
        print('Yes')
    else:
        print('No')
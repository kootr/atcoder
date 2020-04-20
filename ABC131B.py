import numpy as np
N, L = map(int, input().split())
taste = [L+i for i in range(N)]
if L < 0:
    print(sum(taste) + min(np.abs(taste)))
else:
    print(sum(taste) - min(np.abs(taste))) 
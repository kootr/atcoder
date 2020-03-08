# # i for input() in A_1 = list(map(int, input().split()))
import numpy as np
A_1 = [int(i) for i in input().split()]
A_2 = [int(i) for i in input().split()]
A_3 = [int(i) for i in input().split()]
A = np.array([A_1, A_2, A_3])
N = int(input())
b = [int(input()) for i in range(N)]
for i in b:
   A = np.where(A==i,0,A) 

if ((A[0][0]==A[1][1]) and (A[1][1] == A[2][2])):
    print('Yes')
elif ((A[2][0]==A[1][1]) and (A[1][1] == A[0][2])):
    print('Yes')
elif A[0,:].all()==0 or A[:,0].all()==0:
    print('Yes')
elif A[1,:].all()==0 or A[:,1].all()==0:
    print('Yes')
elif A[2,:].all()==0 or A[:,2].all()==0:
    print('Yes')
else:
    print('No')
print(A[2][0])
print(A[1][1])
print(A[0][2])
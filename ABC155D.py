N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = []
for i in range(len(A)):
    for j in range(i+1,len(A)):
        B.append(A[i]*A[j])
B.sort()
print(B[K-1])

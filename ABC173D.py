N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

sum_idx = -(-N // 2)-1
if N % 2 == 0:
    print(sum(A[0:sum_idx+1]) + sum(A[1:sum_idx+1]))
else:
    print(sum(A[0:sum_idx+1]) + sum(A[1:sum_idx])) 

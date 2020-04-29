N = int(input())
A = list(map(int, input().split()))
supervisor_list = list(set(A))
for i in range(1,N+1):
    if i in supervisor_list:
        print(A.count(i))
    else:
        print(0)
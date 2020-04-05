# N = int(input())
# orig_A = list(map(int, input().split()))
# for i in range(N):
#     point = 0
#     A = orig_A.copy()
#     del(A[i])
#     for n in list(set(A)):
#         kosuu = A.count(n)
#         if kosuu >= 2:
#             point += (kosuu*(kosuu-1))/2
#     print(int(point))

N = int(input())
orig_A = list(map(int, input().split()))
set_A = list(set(A))
for i in range(len(set_A)):
    target_kosuu = A.count(set_A(i)) - 1 
    if target_kosuu >= 2:
        point += (target_kosuu*(taget_kosuu-1))/2
        # list(map(str, set(A)).remove(target)
        print(set_A())
    for 
    

for i in range(N):
    point = 0
    A = orig_A.copy()
    del(A[i])

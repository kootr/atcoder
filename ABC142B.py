 N, K = map(int,input().split())
 H = input().split()
 H_i = [int(h) for h in H]

 print(sum(h>=K for h in H_i))

# H = []
# for i in range(N):
#     H = list([int(j) for j in input().split()])
#     H.append(A)


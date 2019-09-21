N, M = [int(i) for i in input().split()]
J = []
for i in range(N):
    A = list([int(j) for j in input().split()])
    J.append(A)

J.sort()
total = 0
for i in range(N):
    if M - J[i][1] < 0:
        total += M * J[i][0]
        break
    else:
        total += J[i][0]*J[i][1]
        M = M - J[i][1]
print(total)

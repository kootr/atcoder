N = int(input())
flag = False
for i in range(1, 10):
    for j in range(i, 10):
        if i * j == N:
            flag = True
    if flag:
        print('Yes')
        break
if not flag:
    print('No')
n = int(input())
cnt = 0
a = []
for i in range(1,n+1,2):
    for j in range(1,i+1):
        if i % j == 0:
            cnt += 1
        else:
            continue
    if cnt == 8:
        a.append(j)
        cnt = 0
    else:
        cnt = 0
print(len(a))

n = int(input())
t1 = 0
x1 = 0
y1 = 0
cnt = 0

for i in range(n):
    t, x, y = map(int, input().split())
    if t - t1  >= (x - x1 + y - y1) and (x - x1 + y - y1 - t + t1) % 2 == 0:
        t1 = t
        x1 = x
        y1 = y
        cnt += 1
        if cnt == n:
            print('Yes')
        else:
            continue
    else:
        print('No')
        exit()

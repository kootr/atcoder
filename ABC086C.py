n = int(input())
for i in range(n):
    t, x, y = map(int, input().split())
    if t >= (x + y) and (x - y) % 2 == 0:
        print('OK')
    else:
        print('NO')
print(t)
print(x)
print(y)

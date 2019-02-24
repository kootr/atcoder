n = input()
d = list(map(int, input().split()))
d.sort()

while d[1] > d[0]:
    d[1] = d[1] - d[0]
    if d[1] == d[0]:
        print(d[0])
        exit()
    elif d[1] < d[0]:
        a = d[1]
        b = d[0]
        d[0] = a
        d[1] = b
    else:
        continue
print(d[1])

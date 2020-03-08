A, B = list(map(int, input().split()))
x = 10*B
cnt = 0
while cnt < 9:
    if int(x*0.08) == A:
        print(x)
        break
    x+=1
    cnt+=1

if cnt == 9:
    print(-1)
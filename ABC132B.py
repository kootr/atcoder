n = int(input())
P = list(map(int, input().split()))
cnt=0
for i in range(n-2):
    p = P[i:i+3]
    p_s = sorted(p)
    if p[1]==p_s[1]:
        cnt+=1
print(cnt)
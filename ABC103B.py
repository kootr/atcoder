s = list(input())
t = list(input())
l = len(s)
cnt=0
for x in range(l):
    if s == t:
        print('Yes')
        break
    else:
        cnt+=1
        s.insert(0, s[-1])
        s=s[:len(s)-1]
if cnt == l:
    print('No')

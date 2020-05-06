S = input()
cnt = 0
tmp = 0

for i in S:
    if  i in ['A', 'C', 'G', 'T']:
        tmp+=1
    elif cnt < tmp:
        cnt = tmp
        tmp = 0
if cnt < tmp:
    print(tmp)
else:
    print(cnt)
    
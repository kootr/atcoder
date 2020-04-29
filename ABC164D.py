S = list(input())
cnt=0
length = len(S)
for i in range(length-3):
    for j in range(i+3,length):
        if S[i] == '0':
            break
        target = int(''.join(S[i:j+1]))
        if target % 2019 == 0:
            cnt+=1
print(cnt)
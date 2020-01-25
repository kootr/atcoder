H = int(input())
cnt=0
sumA=0
while H>1:
    cnt +=1
    H = H // 2
    if H ==1:
        break
for i in range(cnt+1):
    sumA += 2**i
print(sumA)
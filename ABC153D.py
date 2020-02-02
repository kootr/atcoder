H = int(input())
cnt=0
sum_count=0
while H>1:
    cnt +=1
    H = H // 2
    if H ==1:
        break
for i in range(cnt+1):
    sum_count += 2**i
print(sum_count)

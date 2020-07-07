import sys
N = int(input())
evens = [i for i in range(1, N+1) if i%2 ==0]
even_cnts = []
if evens == []:
    print(1)
    sys.exit()
for even in evens:
    cnt = 0
    while even % 2 ==0:
        cnt += 1
        even = even / 2
    even_cnts.append(cnt)
max_cnts = max(even_cnts)
index = even_cnts.index(max_cnts)
print(evens[index])
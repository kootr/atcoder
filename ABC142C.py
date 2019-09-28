N = int(input())
H = [int(h) for h in input().split()]
answer = []
for i in range(1,N+1,1):
    answer.append(H.index(i)+1)
print(' '.join(map(str,answer)))
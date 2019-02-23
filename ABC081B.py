n = input()
a = list(map(int, input().split()))
cnt = 0
while all(b%2==0 for b in a):
    a = [b/2 for b in a]
    cnt +=1
print(cnt)

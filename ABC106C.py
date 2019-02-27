s = input()
k = int(input())
cnt = 0
while s[:1] == '1':
    s = s[1:]
    cnt +=1
if k <= cnt:
    print('1')
else:
    print(s[:1])

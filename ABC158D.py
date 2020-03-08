from collections import deque

S = list(input())
S = deque(S)
Q = int(input())
query = [input().split() for i in range(Q)]
for i in query:
    if i[0] == '1':
        S.reverse()
    elif i[0]=='2' and i[1]=='1':
        S.appendleft(i[2])
    # elif i[0]=='2' and i[1]=='2':
    else:
        S.append(i[2])
print(''.join(list(S)))


s = input()
a = []
sum = 0
for i in s:
    a.append(i)
a_int = [int(t) for t in a]
s_int = int(s)
for j in a_int:
    sum += j
if s_int % sum == 0:
    print('Yes')
else:
    print('No')

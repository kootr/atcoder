a = input()
s = list(a)
s_int = [int(i) for i in s ]
t = len(s_int)
i = 0
c0 = s_int.count(0)
c1 = s_int.count(1)
if c0 > c1:
    print(2*c1)
else:
    print(2*c0)

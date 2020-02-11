N, T = map(int, input().split())
c = []
t = []
for i in range(N):
    c_i, t_i = map(int, input().split())
    c.append(c_i)
    t.append(t_i)
indx =  [i for i, x in enumerate(t) if x <= T]
if len(indx)==0:
    print('TLE')
else:
    c_pass = []
    for i in range(len(indx)):
        c_pass.append(c[indx[i]])
    print(min(c_pass))

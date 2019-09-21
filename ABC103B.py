s = list(input())
t = list(input())
s_list = [ i for i in s ]
t_list = [ i for i in t ]
l = len(s_list)
for x in range(l):
    if s_list == t_list:
        print('Yes')
    else:
        s_list[0] =  s_list[l-1]
        print(s_list)
print('No')

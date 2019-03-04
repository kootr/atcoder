a = input()
s = list(a)
s_int = [int(i) for i in s ]
t = len(s_int)
i = 0
while 0 in s_int and 1 in s_int and i < len(s_int):
    if s_int[i] == 0 and s_int[i+1] == 1:
        s_int.pop(i)
        s_int.pop(i)
    elif s_int[i] == 1 and s_int[i+1] == 0:
        s_int.pop(i)
        s_int.pop(i)
    else:
        i += 1
print(t - len(s_int))

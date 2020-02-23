s = int(input())
A= []
while s not in A:
    A.append(s)
    if s % 2 == 0:
        a_n = s/2
    else:
        a_n = 3*s+1
    s = a_n
print(len(A)+1)
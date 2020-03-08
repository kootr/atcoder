N, A, B = map(int, input().split())
x = N//(A+B)
r = N - (A+B)*x
if r >= A:
    add = A
else:
    add = r

print(x*A + add)
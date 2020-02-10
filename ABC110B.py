N, M, X, Y = map(int, input().split())
# x=[]
# for i in range(N):
#     x.append(int(input()))
x = input().split()
y = input().split()
x = [int(i) for i in x]
y = [int(i) for i in y]
x.sort()
y.sort()
if (x[-1] < y[0]) and (Y >= x[-1]) and (X < y[0]):
    print("No War")
else:
    print("War")

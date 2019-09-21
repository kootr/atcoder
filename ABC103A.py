a = [int(i) for i in input().split()]
a.sort()
cost = 0
for i in range(len(a)-1):
    cost += a[i+1] - a[i]
print(cost)

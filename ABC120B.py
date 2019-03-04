a, b, k = map(int, input().split())
n = 1
list = []
while n <= a and n <=  b:
    if a % n == 0 and b % n == 0:
        list.append(n)
        n += 1
    else:
        n += 1
print(list[-k])

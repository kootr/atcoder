#a, b, c = input().split()
a, b, c = map(int, input().split())

count = 0

while (b >= a) and (c > count):
    b = b - a
    count += 1
print(count)
'''
for i in range(c+1):
    b = b - a
    '''

s = input()
a = []
for i in s:
    a.append(i)
plus = a.count('+')
minus = a.count('-')

print(plus - minus)

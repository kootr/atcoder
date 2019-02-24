n = int(input())
a = list(map(int, [input() for i in range(n)]))
a_unique = len(list(set(a)))
print(a_unique)

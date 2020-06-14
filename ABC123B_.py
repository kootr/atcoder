# A = [int(input()) for i in range(5)]
# print(A)
A = list(map(int, input()))
B = list(map(int, input()))
C = list(map(int, input()))
D = list(map(int, input()))
E = list(map(int, input()))

X = [A, B, C, D, E]
X = [i for i in X if i[-1] != 0]
X.sort(key=lambda x: x[-1], reverse=True)
map = map(str, list)
X = [''.join(i) for i in X]
print(X)
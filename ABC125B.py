N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
benefit=0
for v, c in zip(V, C):
    if v>c:
        benefit += (v-c)
print(benefit)

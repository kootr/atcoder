S = list(input())
cnt = 0
length = len(S) // 2
for i in range(length):
    if S[i] != S[-1-i]:
        cnt += 1
print(cnt)

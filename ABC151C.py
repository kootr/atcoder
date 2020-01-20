#n-1 科目の得点を代入する回数に制限がない
N, M = map(int, input().split(" "))
for i in range(M):
    p, S = input().split(" ")
    p.append(p)
    S.append(S)


#n-1 科目の得点を代入する回数に制限がない
K, X = map(int, input().split(" "))
if 500*K >= X:
    print('Yes')
else:
    print('No')


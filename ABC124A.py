Number= list(map(int, input().split()))
Number.sort()
if Number[0] == Number[1]:
    print(Number.sum())
else:
    print(f'{Number[1]*2 -1}')
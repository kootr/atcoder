Number= list(map(int, input().split()))
Number.sort()
if Number[0] == Number[1]:
    print(sum(Number))
else:
    print(Number[1]*2 -1)
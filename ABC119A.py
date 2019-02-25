s = list(map(int, input().split('/')))

if s[0] < 2019:
    print('Heisei')
elif s[0] == 2019 and s[1] <= 4:
    print('Heisei')
else:
    print('TBD')

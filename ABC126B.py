S = input()

former = S[:2]
later = S[2:]

if int(later) == 0 or int(former) == 0:
    print('NA')
elif int(former) < 13 and int(later) < 13:
    print('AMBIGUOUS')
elif int(former) > 12 and int(later) < 13:
    print('YYMM')
elif int(former) < 13 and int(later) > 12:
    print('MMYY')
else:
    print('NA')
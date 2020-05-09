S = list(input())
odds = S[0::2]
evens = S[1::2]

good_odd = ['R', 'U', 'D']
good_even = ['L', 'U', 'D']

for odd in odds:
    if odd in good_odd:
        pass
    else:
        print('No')
        exit()
for even in evens:
    if even in good_even:
        pass
    else:
        print('No')
        exit()
print('Yes')        
    

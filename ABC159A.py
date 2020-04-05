N, M = map(int, input().split())
if N >=2:
    odd = (N*(N-1))/2
else:
    odd = 0
if M >= 2:
    even = (M*(M-1))/2
else:
    even = 0
print(int(odd+even))
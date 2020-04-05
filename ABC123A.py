N = [int(input()) for i in range(5)]
k = int(input())
if max(N)-min(N) > k:
    print(':(')
else:
    print('Yay!')

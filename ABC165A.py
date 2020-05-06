K = int(input())
A, B = map(int, input().split())
A_shou = A // K
B_shou = B // K
if (A_shou != B_shou) or (A % K == 0):
    print('OK')
else:
    print('NG')
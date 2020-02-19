N = int(input())
A = list(map(int, input().split()))
even_list = [i for i in A if i % 2 == 0]
if len(even_list) == 0:
    print('APPROVED')
else:
    cond_list = [i for i in even_list if (i % 3 == 0) or (i %5 ==0)]
    if len(even_list) == len(cond_list):
        print('APPROVED')
    else:
        print('DENIED')

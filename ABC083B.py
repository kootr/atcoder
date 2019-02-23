j, a, b = map(int, input().split())
sum_all = 0
for n in range(1,j+1):
    n_list_str = list(str(n))
    n_list_int = [int(i) for i in n_list_str]
    sum = 0
    for i in range(len(n_list_int)):
        sum += n_list_int[i]
    if  a <= sum <= b:
        sum_all += n
print(sum_all)

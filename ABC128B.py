N = int(input())
rest_list = []
for i in range(N):
    a,b=input().split()
    temp=[i+1,a,(-1)*int(b)]
    rest_list.append(temp)
rest_list.sort(key=lambda x: (x[1], x[2]))
for i in rest_list:
    print(i[0])

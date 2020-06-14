X = int(input())
count_500 = X // 500
count_5 = (X - 500*count_500) // 5

print(count_500*1000+count_5*5)
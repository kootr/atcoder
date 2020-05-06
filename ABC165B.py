X = int(input())
year = 0
amount = 100
while amount < X:
    amount = int(amount*1.01)
    year += 1
print(year)
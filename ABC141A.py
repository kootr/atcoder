S = input()
whether = ['Sunny', 'Cloudy', 'Rainy']
i = whether.index(S)
if i == 2:
    print(whether[0])
else:
    print(whether[i+1])
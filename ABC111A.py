n = list(input())
n_opp = [ '1' if i=='9' else '9' for i in n]
n_opp = ''.join(n_opp)
print(n_opp)

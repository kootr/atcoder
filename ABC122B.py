import re
S = input()
# for i in range(S):
ans = [m.span() for m in re.finditer('[ACGT]', S)]

print(list(ans))

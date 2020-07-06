N = int(input())
S = []
C = []
for i in range(N):
    S.append(input())

results = ['AC', 'WA', 'TLE', 'RE']
for result in results:
    C.append(S.count(result))
print(f"AC x ",C[0],
"\nWA x ",C[1],
"\nTLE x ",C[2],
"\nRE x ",C[3]
)   
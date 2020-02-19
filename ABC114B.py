S = input()
S = list(S)
A = []
for i in range(len(S)-2):
    target_num = ''.join(S[i:i+3])
    A.append(abs(753 - int(target_num)))
print(min(A))
    
def minus26(idx):
    while idx >= 26:
        idx = idx - 26
    return idx
    
N = int(input())
S = list(input())

alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

S_idx = [alphabet.index(s)+N for s in S] 
S_idx = [minus26(idx) for idx in S_idx]
print(''.join([alphabet[idx] for idx in S_idx]))

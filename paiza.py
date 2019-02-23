input_lines = int(input())
hantei = [''] * input_lines
s = 0
b = 0

for i in range(input_lines):
    hantei[i] = input()
    if hantei[i] == 'strike':
        s +=1
    else:
        b +=1
    if s == 3:
        print('out!')
        break
    if b == 4:
        print('fourball!')
        break
    print(hantei[i]+'!')

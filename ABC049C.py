import re
s = input()
while len(s) > 0:
    if s.startswith('dreameraser'):
        s = re.sub('^dreameraser', '',s)
    elif s.startswith('dreamerase'):
        s = re.sub('^dreamerase', '',s)
    elif s.startswith('dreamer'):
        s = re.sub('^dreamer', '',s)
    elif s.startswith('dream'):
        s = re.sub('^dream', '',s)
    elif s.startswith('eraser'):
        s = re.sub('^eraser', '',s)
    elif s.startswith('erase'):
        s = re.sub('^erase', '',s)
    else:
        print('NO')
        exit()
print('YES')

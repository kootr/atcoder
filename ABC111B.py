n = list(input())
n = [int(i) for i in n] 
if n[0]>n[1] or (n[0]==n[1] and n[0]>=n[2]):
    print(str(n[0])*3)
elif n[0]<n[1] or (n[0]==n[1] and n[0]<n[2]):
    print(str(n[0]+1)*3)
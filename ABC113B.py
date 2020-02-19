N = int(input())
T, A = map(int, input().split())
H = [int(i) for i in input().split()]
S = [abs(T-(0.006)*i-A) for i in H]
print(S.index(min(S))+1)
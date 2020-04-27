N = int(input())
fizzbuzz = [i for i in range(1, N+1) if (i % 3 == 0) or (i % 5 == 0)]

print(int(N*(N+1)/2 - sum(fizzbuzz)))
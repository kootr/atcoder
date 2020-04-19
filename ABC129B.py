N = int(input())
W = list(map(int, input().split()))
score = [abs(sum(W[:index]) - sum(W[index:])) for index in range(N)]
print(min(score))
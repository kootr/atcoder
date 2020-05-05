A, B, N = map(int, input().split())
max_value=0
for x in range(1, N+1):
    test_value = int(A*x/B) - A*int(x/B)
    if test_value > max_value:
        max_value = test_value
print(max_value)
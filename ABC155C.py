import collections
N = int(input())
S = [input() for i in range(N)]
c = collections.Counter(S)
max_count = c.most_common()[0][1]
max_k_list = [kv[0] for kv in c.items() if kv[1] == max_count]
max_k_list.sort()
for max_k in max_k_list:
    print(max_k)

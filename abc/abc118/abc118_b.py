# https://atcoder.jp/contests/abc118/tasks/abc118_b

N, M = map(int, input().split())

dict = {}
for n in range(N):
    k_a = [int(_) for _ in input().split()]
    for k in range(k_a[0]):
        if k_a[k+1] in dict:
            dict[k_a[k+1]] += 1
        else:
            dict[k_a[k+1]] = 1

count = 0
for key in dict:
    if dict[key] == N:
        count += 1

print(count)
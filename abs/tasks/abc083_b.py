# https://atcoder.jp/contests/abs/tasks/abc083_b

N, A, B = map(int, input().split())

total = 0
for n in range(N + 1):
    if n < A:
        continue
    n_list = [int(_) for _ in list(str(n))]
    n_sum = sum(n_list)
    if A <= n_sum <= B:
        total += n

print(total)
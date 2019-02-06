# https://atcoder.jp/contests/abc115/tasks/abc115_b

N = int(input())

p = list()
for n in range(N):
    p.append(int(input()))

p.sort(reverse=True)

max_val = p.pop(0) / 2
print(int(sum(p) + max_val))
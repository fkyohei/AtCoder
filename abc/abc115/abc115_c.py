# https://atcoder.jp/contests/abc115/tasks/abc115_c

N, K = map(int, input().split())

H = list()
for n in range(N):
    H.append(int(input()))

H.sort(reverse=True)

diff = list()
for n in range(N-K+1):
    diff.append(H[n] - H[n+K-1])

diff.sort()
print(diff.pop(0))
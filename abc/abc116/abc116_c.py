# https://atcoder.jp/contests/abc116/tasks/abc116_c

N = int(input())
H = [int(_) for _ in input().split()]

count = 0
while True:
    for n in range(N):
        if H[n] == 0:
            continue
        elif n == N-1:
            count += 1
        elif H[n+1] == 0:
            count += 1
        H[n] -= 1
    if sum(H) == 0:
        break
print(count)
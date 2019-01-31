import sys

N, Y = map(int, input().split())

for b10_count in range(0, N+1):
    for b5_count in range(0, N+1-b10_count):
        b1_count = N - b10_count - b5_count
        sum = 10000 * b10_count + 5000 * b5_count + 1000 * b1_count
        if sum == Y:
            print(b10_count, b5_count, b1_count)
            sys.exit()

print(-1, -1, -1)

## 3重ループで全探索するとタイムアウトする
## 2つ枚数が決まった時点で、3つ目は総枚数から差し引くことで導けることを気づけるかどうか
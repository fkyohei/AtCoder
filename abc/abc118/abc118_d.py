# https://atcoder.jp/contests/abc118/tasks/abc118_d

cost = {
    1: 2,
    2: 5,
    3: 5,
    4: 5,
    5: 4,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

N, M = map(int, input().split())
A = [int(_) for _ in input().split()]
C = [cost[i] for i in A]

# 途中
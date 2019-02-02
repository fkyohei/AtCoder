# https://atcoder.jp/contests/abs/tasks/abc081_b

import sys

N = int(input())
# 内包表記
input_list = [int(_) for _ in input().split()]

count = 0
while True:
    for index in range(N):
        if input_list[index] % 2 == 0:
            input_list[index] /= 2
        else:
            print(count)
            sys.exit()
    count += 1
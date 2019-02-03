# https://atcoder.jp/contests/abc117/tasks/abc117_c

import sys

N, M = map(int, input().split())
X = [int(_) for _ in input().split()]

# 座標数よりコマ数が多ければ初期位置で条件を満たす
if N >= M:
    print(0)
    sys.exit()

# ソートする
X.sort()

# 隣り合う数の差を計算する
diff = list()
for m in range(M-1):
    diff.append(X[m+1] - X[m])

# for n in range(N-1):
#     max_index = diff.index(max(diff))
#     diff.pop(max_index)
# print(sum(diff))
diff.sort(reverse=True)
print(sum(diff[N-1:]))
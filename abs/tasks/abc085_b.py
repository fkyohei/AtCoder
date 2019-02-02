# https://atcoder.jp/contests/abs/tasks/abc085_b

N = int(input())

d_list = []
for n in range(N):
    d_list.append(int(input()))

d_list.sort(reverse=True)

count = 1
top = d_list[0]
for d in d_list:
    if d >= top:
        continue
    top = d
    count += 1

print(count)

## 並び変えなくても重複排除して個数を数えれば同じ答えが得られる
## リストの重複排除はset(変数名)
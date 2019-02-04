# https://atcoder.jp/contests/abc116/tasks/abc116_b
import sys

S = int(input())

a = list()
a.append(0)
a.append(S)

i = 2
while True:
    if a[i-1] % 2 == 0:
        n = a[i-1] / 2
    else:
        n = 3 * a[i-1] + 1
    n = int(n)
    for l in range(len(a)-1):
        if a[l] == n:
            print(i)
            sys.exit()
    
    a.append(n)
    i += 1

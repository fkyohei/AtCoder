# https://atcoder.jp/contests/abc117/tasks/abc117_b

N = int(input())
L = [int(_) for _ in input().split()]
L.sort(reverse=True)
 
if L.pop(0) < sum(L):
    print('Yes')
else:
    print('No')
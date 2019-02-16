# https://atcoder.jp/contests/abc118/tasks/abc118_c

import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

N = int(input())
A = [int(_) for _ in input().split()]

print(gcd_list(A))
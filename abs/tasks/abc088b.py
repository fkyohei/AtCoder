N = int(input())
a_list = [int(_) for _ in input().split()]

# 降順に並び替える
a_sorted_list = sorted(a_list, reverse=True)

alice = bob = 0
for index, val in enumerate(a_sorted_list):
    if index % 2 == 0:
        alice += val
    else:
        bob+= val
# 差を求める
diff = alice - bob
print(diff)

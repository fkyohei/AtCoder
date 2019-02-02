import sys

N = int(input())

step = 0
current_x = 0
current_y = 0
for n in range(N):
    t, x, y = map(int, input().split())
    distance = abs(x - current_x) + abs(y - current_y)
    step_diff = t - step
    # ステップ数よりも距離が遠い場合はたどり着けない
    if distance > step_diff:
        print('No')
        sys.exit()
    
    # step数と距離がどちらも奇数またはどちらも偶数であればたどり着ける
    if (step_diff % 2 == 1 and distance % 2 == 1) or (step_diff % 2 == 0 and distance % 2 == 0):
        step = t
        current_x = x
        current_y = y
        continue

    # ここまで来た場合はたどり着けない
    print('No')
    sys.exit()

# ここまで来た場合は最終地点まで行ける
print('Yes')
A = int(input()) # 500円玉枚数
B = int(input()) # 100円玉枚数
C = int(input()) # 50円玉枚数
X = int(input()) # 合計金額

count = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            total = 500 * a + 100 * b + 50 * c
            if total == X:
                count += 1

print(count)
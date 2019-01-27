a = int(input())
b, c = map(int, input().split())
s = input()

#print((a + b + c), s)
# フォーマット指定の出力はこのほうが良い
print("{} {}".format((a + b + c), s))
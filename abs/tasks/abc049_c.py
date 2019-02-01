import sys
S = input().strip()

word_list = ['dreamer', 'eraser', 'dream', 'erase']

while True:
    flag = False
    for w in word_list:
        length = len(w)
        if w == S[-length:]:
            S = S[:-length]
            flag = True
            if S == '':
                print('YES')
                sys.exit()

    if flag == False:
        break

print('NO')

# 「er」がderamerの末尾とerace/erのerがあるため、前方からじゃなく後方からやるのがポイント
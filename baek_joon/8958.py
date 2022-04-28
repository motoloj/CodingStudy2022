# 2022_04_28_1
# OX퀴즈
for _ in range(int(input())):
    quiz = input()
    total, count = 0, 0 
    for i in quiz:
        if i == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)
# 2022_04_27_1
# Baseball
for _ in range(int(input())):
    total_y, total_k = 0, 0
    for _ in range(9):
        y, k = map(int, input().split())
        total_y += y
        total_k += k
    if total_y > total_k:
        print("Yonsei")
    elif total_y < total_k:
        print("Korea")
    else:
        print("Draw")
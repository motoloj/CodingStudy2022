# 2022_02_24_1
# 윷놀이
for _ in range(3):
    game = list(map(int, input().split()))
    count = sum(game)
    if count == 4: # 모
        print("E")
    elif count == 3:
        print("A")
    elif count == 2:
        print("B")
    elif count == 1:
        print("C")
    elif count == 0: # 윷
        print("D")
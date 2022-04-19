# 2022_04_19_2
# 알파벳 거리

for _ in range(int(input())):
    word1, word2 = input().split()
    distance_list = []
    for i in range(len(word1)):
        x = ord(word1[i]) - 64
        y = ord(word2[i]) - 64
        if x <= y:
            result = y - x
        else:
            result = (y+26) - x
        distance_list.append(result)
    print("Distances:", *distance_list)

# PRINT(A, B) => A B 한 칸 뛴 채로 출력
        
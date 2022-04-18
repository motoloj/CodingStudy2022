# 2022_04_18_1
# 알파벳 개수
alphabet = [0]*26
for i in input().upper():
    n = ord(i) - 65
    alphabet[n] += 1
print(*alphabet)
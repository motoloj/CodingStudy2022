# 2022_04_02_1
# 알파벳 찾기
# chr(아스키코드값) = 문자, ord(문자) = 아스키코드값
alpha = [-1]*26
word = input()
sort_word = set(word)
for i in sort_word:
    alpha[ord(i)-97] = word.find(i)
print(*alpha)
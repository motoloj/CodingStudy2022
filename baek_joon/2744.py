# 2022_04_08_1
# 대소문자 바꾸기
word = input()
ans = ''
for i in word:
    if i.isupper() == True:
        ans += i.lower()
    else:
        ans += i.upper()
print(ans)
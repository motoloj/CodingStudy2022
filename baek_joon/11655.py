# 2022_04_23_1
# ROT13
# ord 'A~Z' = 65~90, a~z = 97~122
word = input()
new_word = ''
for i in word:
    if i.isupper() == True:
        Rot13 = ord(i) + 13
        if Rot13 > 90: 
            Rot13 = chr(Rot13 - 90 + 65 - 1)
        new_word += chr(Rot13)
        
    elif i.islower():
        Rot13 = ord(i) + 13
        if Rot13 > 122:
            Rot13 = chr(Rot13 - 122 + 97 -1)
        new_word += chr(Rot13)
        
    else:
        new_word += i
print(new_word)

# 다른 풀이, 알파벳 중간 m과 알파벳 절반수 13 이용
word = input()
new_word = ''
for i in word:
    if 'a' <= i <= 'z':
        new_word += chr((ord(i)+13) if i <= 'm' else ord(i)-13)
    elif 'A' <= i <= 'Z':
        new_word += chr((ord(i)+13) if i <= 'M' else ord(i)-13)
    else:
        new_word += i
print(new_word)
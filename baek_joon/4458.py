# 2022_04_13_1
# 첫 글자를 대문자로
# str은 튜플 처럼 수정불가 자료구조(immutable type)
# 리스트 사용 후 조인 하거나, replace 사용
for _ in range(int(input())):
    sentence = list(input())
    sentence[0] = sentence[0].upper()
    print(''.join(sentence))

# 2022_04_16_1
# 열 개씩 끊어 출력하기
word = input()
print(*[word[i:i+10] for i in range(0,len(word),10)],sep='\n')
# 출력리스트 혹은 for문 범위를 잘못할 경우 공백생성

# 2022_04_19_1
# 단어 공부
# Counter 큰 순서대로 정렬 됨(튜플 형태, sorted key=lambda x: x[0] 정렬가능. 해당 문제와는 연관 X)
# 빈도수 가장 높은 것이 한 개거나 한개이면서 여러 빈도수를 포함할 때 // 빈도수 가장 높은 것이 2개이상일 케이스 
from collections import Counter

count_alpabet = Counter(input().upper()).most_common(n=2)
print(count_alpabet)
print(len(count_alpabet))
if len(count_alpabet) == 2: # 같은 출력 케이스를 묶는 것 보다 리스트 길이에 따라 경우를 분류해서 출력
    
    if count_alpabet[0][1] > count_alpabet[1][1]:
        print(count_alpabet[0][0])
    else:
        print('?')
else:
    print(count_alpabet[0][0])
    
# 1 X count_alpabet[0][0]

# 2 2 '?'

# 2 > 1 count_alpabet[0][0]


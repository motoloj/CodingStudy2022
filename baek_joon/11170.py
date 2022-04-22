# 2022_04_22_1
# 0의 개수
# 10배수로 처리하는 것 고민 -> 문자열 처리로 변경
# 시간 4408ms 소요
for _ in range(int(input())):
    count = 0
    n, m = map(int, input().split())
    for i in range(n, m+1):
        for g in str(i):
            if g == '0':
                count += 1
    print(count) 
    
# count 함수 사용 => 리스트나 문자열 에서 사용
for _ in range(int(input())):
    count = 0
    n, m = map(int, input().split())
    for i in range(n, m+1):
        count += str(i).count('0')
    print(count) 
# 2856ms 소요